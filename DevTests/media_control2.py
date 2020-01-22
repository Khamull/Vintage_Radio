import dbus, dbus.mainloop.glib, sys
from RPi import GPIO
from time import sleep
from gi.repository import GLib
 
btn = 22

def on_property_changed(interface, changed, invalidated):
    if interface != 'org.bluez.MediaPlayer1':
        return
    for prop, value in changed.items():
        if prop == 'Status':
            print('Playback Status: {}'.format(value))
        elif prop == 'Track':
            print('Music Info:')
            for key in ('Title', 'Artist', 'Album'):
                print('   {}: {}'.format(key, value.get(key, '')))
 
def on_playback_control(condition):
    print("Button was pushed")
    str = "next"
    if str.startswith('play'):
        player_iface.Play()
    elif str.startswith('pause'):
        player_iface.Pause()
    elif str.startswith('next'):
        player_iface.Next()
    elif str.startswith('prev'):
        player_iface.Previous()
    return True
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
 
    bus.add_signal_receiver(
            on_property_changed,
            bus_name='org.bluez',
            signal_name='PropertiesChanged',
            dbus_interface='org.freedesktop.DBus.Properties')
    #GLib.io_add_watch(sys.stdin, GLib.IO_IN, on_playback_control)
    GPIO.add_event_detect(btn,GPIO.RISING,callback=on_playback_control, bouncetime=300)
    GLib.MainLoop().run()
