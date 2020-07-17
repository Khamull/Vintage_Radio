#test of different button presses!
#Lets hope for the best!
#https://raspberrypi.stackexchange.com/questions/99645/getting-button-click-type

import config as cf
import RPi.GPIO as GPIO
import time
import threading

BtnPin = cf.l_btn # GPIO pin

timeout = 0.5 # how long can pass between two clicks to consider them part of the same event
short_click = 0.65 # length of a single click
long_click = 1.0 # length of a long click
very_long_click = 4.0 # length of a veeeery long click

# set up the GPIO pins to register the presses
GPIO.setmode(GPIO.BCM)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input

# returns the kind ok click
def pressed():
    start_time = time.time()
    while not GPIO.input(BtnPin):
        time.sleep(.1)
    pressed_time = time.time() - start_time
    if pressed_time < short_click:
        return 'short'
    elif pressed_time > very_long_click:
        return 'very long'
    else:
        return 'long'

# returns the kind of click event
def pressing():
    global clicks
    tmpclicks = []
    start_time = time.time()
    while time.time() - start_time < timeout:
        if not GPIO.input(BtnPin):
            tmpclicks.append(pressed())
            start_time = time.time()
    clicks = tmpclicks

clicks = [] # set up an empty list for the kind of clicks

lasting = 0

while True:
    #print (lasting) # just to show you can do other while getting the clicks
    lasting +=1
    # we create a thread for getting click events so we can other while waiting for the clicks
    try:
        t
    except NameError:
        if not GPIO.input(BtnPin):
            t= threading.Thread(target=pressing)
            t.start()
    else:
        if clicks:
            if clicks == ['short']:
                print ("Single click")
            elif clicks == ['short', 'short']:
                print ("Double click")
            elif clicks == ['short','short', 'short']:
                print ("Triple click")
            elif clicks == ['long']:
                print ("Long click")
            elif clicks == ['long', 'long']:
                print ("Double long click")
            elif clicks == ['very long']:
                print ("Very long click")
            clicks = []
            del t