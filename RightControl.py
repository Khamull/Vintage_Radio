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
#    if not adapter:
#        Sys.exit('Error: Media Player not found.')
    try:
        while True:
            #print("Started")
            btnPushed = GPIO.input(btn)
            if ((not btnLastState) and btnPushed):
                if isPaused:
                    isPaused = False
                    print("Play")
                    player_iface.Play()
                    sleep(1)
                else:
                    isPaused = True
                    print("Pause")
                    player_iface.Pause()
                    sleep(1)
            else:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                    if isPaused:
                        isPaused = False
                    if dtState != clkState:
                        player_iface.Next()
                        print("Next")
                        sleep(0.9)
                    else:
                        player_iface.Previous()
                        print("Previous")
                        sleep(0.9)

                clkLastState = clkState
            btnLastState = btnPushed
    finally:
        GPIO.cleanup()
    
    




