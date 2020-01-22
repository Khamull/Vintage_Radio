from RPi import GPIO
from time import sleep
import subprocess

clk = 27
dt = 17
btn = 22

# vals from output of amixer cget numid=1
min = 0
max = 6000

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

isMuted = False
preVolume = volume = 85  # give it some volume to start with
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)

#amixer set Master 50%

subprocess.call(['amixer', 'set', 'Master', str(volume)+"%"])

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
            subprocess.call(['amixer', 'set', 'Master', str(volume)+"%"])
            sleep(0.05)
        else:
            clkState = GPIO.input(clk)
            dtState = GPIO.input(dt)
            if clkState != clkLastState:
                if isMuted:
                    isMuted = False
                    volume = 0
                if dtState != clkState:
                    volume += 5
                    if volume > max:
                        volume = max
                else:
                    volume -= 5
                    if volume < min:
                        volume = min
                print ("{:d} ({:.0%})".format(volume, float(volume)/float(max)))
                subprocess.call(['amixer', 'set', 'Master', str(volume)+"%"])
            clkLastState = clkState
        btnLastState = btnPushed
finally:
    GPIO.cleanup()