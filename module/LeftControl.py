#!/usr/bin/python3
from RPi import GPIO
import config as cf
from subprocess import DEVNULL, STDOUT, check_call



clk = 22
dt = 27
btn = 17

# vals from output of amixer cget numid=1
min = 0
max = 100
step = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

isMuted = False
preVolume = volume = cf.volume # give it some volume to start with
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)

def volume_callback(channel):
    global preVolume, volume, isMuted, clkLastState
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if isMuted:
            isMuted = False
            volume = 0
        if dtState != clkState:
            volume += step
            if volume > max:
                volume = max
            cf.volume = volume
        else:
            volume -= step
            if volume < min:
                volume = min
            cf.volume = volume
        print("Volume ({:.0%})".format(float(volume)/float(max)), end="\r")
        command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
        check_call(command, stdout=DEVNULL, stderr=STDOUT)
    clkLastState = clkState

def set_volume(volume):
    command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
    check_call(command, stdout=DEVNULL, stderr=STDOUT)

def button_callback(channel):
    global btnLastState
    global preVolume
    global volume
    global isMuted
    btnPushed = GPIO.input(btn)
    if isMuted:
        volume = preVolume
        isMuted = False
        cf.volume = volume
        print("Unmuted")
    else:
        preVolume = volume
        volume = 0
        isMuted = True
        cf.volume = volume
        print("Muted")
    command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
    check_call(command, stdout=DEVNULL, stderr=STDOUT)
    btnLastState = btnPushed

def main():
    #amixer set Master the volume defined in config
    #amixer -c 0  cset numid=1 100%
    #command = ["amixer", "-c", "0", "cset", "numid=1", "{}%".format(volume)]
    command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
    check_call(command, stdout=DEVNULL, stderr=STDOUT)
    print("Volume ({:.0%})".format(float(volume)/float(max)), end="\r")

#adding event listener for click
GPIO.add_event_detect(btn,GPIO.RISING,callback=button_callback, bouncetime=300)
#listening for a input to be able to mesure both!
GPIO.add_event_detect(clk,GPIO.FALLING,callback=volume_callback,bouncetime=4)   

