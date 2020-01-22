#!/usr/bin/python3
from RPi import GPIO
from time import sleep

from subprocess import DEVNULL, STDOUT, check_call
import sys

clk = 27
dt = 22
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
preVolume = volume = 50 # give it some volume to start with
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)

#amixer set Master 50%
#amixer -c 0  cset numid=1 100%
#command = ["amixer", "-c", "0", "cset", "numid=1", "{}%".format(volume)]
command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
check_call(command, stdout=DEVNULL, stderr=STDOUT)
print("Volume ({:.0%})".format(float(volume)/float(max)), end="\r")
try:
    while True:
        btnPushed = GPIO.input(btn)
        if ((not btnLastState) and btnPushed):
            if isMuted:
                volume = preVolume
                isMuted = False
                print("Unmuted")
            else:
                preVolume = volume
                volume = 0
                isMuted = True
                print("Muted")
            command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
            check_call(command, stdout=DEVNULL, stderr=STDOUT)
        else:
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
                else:
                    volume -= step
                    if volume < min:
                        volume = min
                print("Volume ({:.0%})".format(float(volume)/float(max)), end="\r")
                command = ["amixer", "cset", "numid=3", "{}%".format(volume)]
                check_call(command, stdout=DEVNULL, stderr=STDOUT)
            clkLastState = clkState
        btnLastState = btnPushed
finally:
    GPIO.cleanup()
