import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
adapter = None 
def on_property_changed(interface, changed, invalidated):
#     if interface != 'org.bluez.MediaPlayer1':
#         return
    for prop, value in changed.items():
        if prop == 'Status':
            print('Playback Status: {}'.format(value))
        elif prop == 'Track':
            print('Music Info:')
            for key in ('Title', 'Artist', 'Album'):
                print('   {}: {}'.format(key, value.get(key, '')))
 
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
        if not adapter:
            sys.exit('Error: Media Player not found.')
 
    bus.add_signal_receiver(
            on_property_changed,
            bus_name='org.bluez',
            signal_name='PropertiesChanged',
            dbus_interface='org.freedesktop.DBus.Properties')
    GLib.MainLoop().run()