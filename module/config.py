# -*- coding: utf-8 -*-
# file created to share global variables troughout modules!
# will probably read and right to a config file!

#import ConfigController as cf

#todo: source selection
source = 0

if source == 0:
    #volume variables
    interval = 80
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


#status variable :todo, get the latest and save the current!
status = "pause"

#music info, for now, only from bluetooth
music_info = ""
next_music_info =  ""
#status messages in errors cases
message = ""


#initial musics folder
initFolder = "/home/pi/Music/"
USBFolder = ""
