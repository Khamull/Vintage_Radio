import os # allow us to access OS functions
import time # allow us to access time functions
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


_count = 0
def button_callback(channel):
    global _count
    _count = _count + 1
    print("Button was pushed this many times " + str(_count))

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback, bouncetime=300) # Setup event on pin 7 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up