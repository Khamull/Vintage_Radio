# -*- coding: utf-8 -*-
# file created to share global variables troughout modules!
# will probably read and right to a config file!

#import ConfigController as cf

#todo: source selection
source = 0
defaultStart = 1#0 to menu, 1 to Local MP#, 2 To Bluetooth(have tom implement yet)
interval_r = 0
if source == 0:
    #volume variables
    interval = 50
    lastVolume = 0
    min = 0
    max = 100
    step = 5
if source == 1:
#menu variables
    interval = 0
    min = 0
    max = 100
    step = 5

#left rotary config
l_clk    = 22
l_dt     = 27
l_btn    = 17

#right rotary config
r_clk    = 26
r_dt     = 6
r_btn    = 13



#status variable :todo, get the latest and save the current!
status = "pause"
second_status = ""

#music info, for now, only from bluetooth
music_info = []
next_music_info =  ""
#status messages in errors cases
message = ""


#initial musics folder
initFolder  = "/home/pi/Music/"
USBFolder   = ""
#local player variables
musicName   = ""
artist      = ""
album       = ""
time        = ""