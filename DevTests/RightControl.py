#! /usr/bin/env python
#Devera ser responsavel por pular musicas
#Voltar Musicas
#Pausar e Play
#Displays music Info
import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
from RPi import GPIO
from time import sleep

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

isPaused = False
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object('org.bluez', "/")
    mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
    for path, ifaces in mgr.GetManagedObjects().items():
        adapter = ifaces.get('org.bluez.MediaPlayer1')
        if not adapter:
            continue
        player = bus.get_object('org.bluez',path)
        player_iface = dbus.Interface(
                player,
                dbus_interface='org.bluez.MediaPlayer1')
        break
    if not adapter:
        sys.exit('Error: Media Player not found.')
 
      
    try:
        while True:
            btnPushed = GPIO.input(btn)
            if ((not btnLastState) and btnPushed):
                if isPaused:
                    isPaused = False
                    print("Play")
                    player_iface.Play()
                else:
                    isPaused = True
                    print("Pause")
                    player_iface.Pause()
                sleep(0.05)
            else:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                    if isPaused:
                        isPaused = False
                    if dtState != clkState:
                        player_iface.Next()
                        print("Next")
                    else:
                        player_iface.Previous()
                        print("Previous")

                clkLastState = clkState
            btnLastState = btnPushed
    finally:
        GPIO.cleanup()
    
    




