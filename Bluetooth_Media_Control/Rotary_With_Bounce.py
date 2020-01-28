from RPi import GPIO
from time import sleep

clk = 6
# dt = 26
# btn = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

clkLastState = GPIO.input(clk)

def next_callback(channel):
    print("Encoder was turned")
     
#clkLastState = GPIO.input(clk)
GPIO.add_event_detect(6, GPIO.RISING, callback=next_callback, bouncetime=300)

