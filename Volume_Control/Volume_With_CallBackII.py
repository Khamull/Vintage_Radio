import RPi.GPIO as GPIO
from subprocess import DEVNULL, STDOUT, check_call

isMuted = False
btn = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
btnLastState = GPIO.input(btn)
preVolume = volume = 50 # give it some volume to start with

def button_callback(channel):
    global btnLastState
    global preVolume
    global volume
    global isMuted
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
GPIO.add_event_detect(btn,GPIO.RISING,callback=button_callback, bouncetime=150)