#!/usr/bin/python
#Devera ser responsavel por pular musicas
#Voltar Musicas
#Pausar e Play

#import dbus, dbus.mainloop.glib
from RPi import GPIO
import config as cf

clk = 26
dt = 6
btn = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)


isPaused = False
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)
adapter = None

def pause_button_callback(channel):
    global isPaused, player_iface, btnLastState
    btnPushed = GPIO.input(btn)
    if isPaused:
        player_iface.Play()
        isPaused = False
        print("Play")
        cf.status = "play"
    else:
        player_iface.Pause()
        isPaused = True
        print("Pause")
        cf.status = "pause"
    btnLastState = btnPushed

def next_callback(channel):
    global clkLastState
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if dtState != clkState:
            player_iface.Next()
            print("Next")
    clkLastState = clkState


def prev_callback(channel):
    global clkLastState
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if dtState != clkState:
            player_iface.Previous()
            print("Previous")
    clkLastState = clkState

GPIO.add_event_detect(clk,GPIO.FALLING,callback=next_callback)
GPIO.add_event_detect(dt,GPIO.FALLING,callback=prev_callback)
GPIO.add_event_detect(btn,GPIO.FALLING,callback=pause_button_callback,bouncetime=300)

def main():
 pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass





