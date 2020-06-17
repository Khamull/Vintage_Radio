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
step = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)


clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)
interval = 0

isReseted = False
preInterval = interval = cf.interval # give it some interval to start with


def option_callback(channel):
    global preInterval, interval, isReseted, clkLastState, interval
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if isReseted:
            isReseted = False
            interval = 0
        if dtState != clkState:
            interval += step
            if interval > max:
                interval = max
            cf.interval = interval
            print(interval)
        else:
            interval -= step
            if interval < min:
                interval = min
            cf.interval = interval
            print(interval)
        print(interval)
    interval = interval
    clkLastState = clkState

def button_callback(channel):
    global btnLastState
    global interval
    btnPushed = GPIO.input(btn)
    if(interval >= 0 and interval <=25):
        print("Selected option 1")
    if(interval >= 26 and interval <=50):
        print("Selected option 2")
    if(interval >= 51 and interval <=75):
        print("Selected option 3")
    if(interval >= 76 and interval <=100):
        print("Selected option 4")
    btnLastState = btnPushed

#adding event listener for click
GPIO.add_event_detect(btn,GPIO.RISING,callback=button_callback, bouncetime=300)
#listening for a input to be able to mesure both!
GPIO.add_event_detect(clk,GPIO.FALLING,callback=option_callback,bouncetime=4)   

def main():
    print(interval)

