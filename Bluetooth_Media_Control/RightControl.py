#!/usr/bin/python
#Devera ser responsavel por pular musicas
#Voltar Musicas
#Pausar e Play

import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
from RPi import GPIO
from time import sleep

clk = 6
dt = 26
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
    global isPaused, player_iface
    btnPushed = GPIO.input(btn)
    if isPaused:
        player_iface.Play()
        isPaused = False
        print("Play")
    else:
        player_iface.Pause()
        isPaused = True
        print("Pause")
    btnLastState = btnPushed

def next_prev_callback(channel):
    global isPaused, clkLastState, btnLastState, player_iface
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if isPaused:
            isPaused = False
        if dtState != clkState:
            #sleep(0.005)
            if GPIO.input(dt) == 0:
                player_iface.Next()
                print("Next")
                #sleep(0.9)
        else:
            #sleep(0.005)
            if GPIO.input(clk) == 0:
                player_iface.Previous()
                print("Previous")
                #sleep(0.9)
    clkLastState = clkState
    
    
if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object('org.bluez', "/")
    mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
    while not adapter:
        for path, ifaces in mgr.GetManagedObjects().items():
            adapter = ifaces.get('org.bluez.MediaPlayer1')
            if not adapter:
                continue
            player = bus.get_object('org.bluez',path)
            player_iface = dbus.Interface(
                    player,
                    dbus_interface='org.bluez.MediaPlayer1')
            break
        
GPIO.add_event_detect(clk,GPIO.FALLING,callback=next_prev_callback,bouncetime=10)
GPIO.add_event_detect(btn,GPIO.FALLING,callback=pause_button_callback,bouncetime=300)
try:
    while True:
        pass
finally:
    GPIO.cleanup() 




