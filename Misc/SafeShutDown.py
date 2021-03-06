#!/usr/bin/env python3.7
#SCRITP TO Safely shutdown the pi
import os # allow us to access OS functions
import time # allow us to access time functions
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM) # use GPIO numbering
GPIO.setwarnings(False)
btn = 17
# use a weak pull_up to create a high
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    print("starting process")
    while True:
        print("While Runing")
        # set an interrupt on a falling edge and wait for it to happen
        GPIO.wait_for_edge(btn, GPIO.FALLING)
        # we got here because the button was pressed.
        # wait for 3 seconds to see if this was deliberate
        start_time = time.time()
        pushTime = 0
        while pushTime < 5000:
          print("Button Was Pushed: pushTime = " + str(pushTime))
          time.sleep(0.1)
          if GPIO.input(btn) == 0:
                pushTime = pushTime + 100 
          else:
              pushTime = 0
        end_time = time.time()
        _time = end_time-start_time
        print("Button has been pushed and held for 5000 ms with total time: "+str(_time))
        subprocess.Popen(['poweroff'], shell=True, \
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #sleep(3)
        # check the button level again
        #if GPIO.input(INT) == 0:
            # still pressed, it must be a serious request; shutdown Pi
            #subprocess.call(['poweroff'], shell=True, \
                #stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    main()

         
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
