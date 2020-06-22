#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

#   The ideia is simple ply a given audio file
#   The commandas shoudl all be the same interface
#   The ability to navigate in folders and access specific
#   songs might be a good addon, also shuffle and repeat


import vlc
import time
import FilesControll as fc
#song = "/home/pi/Music/114-big_brother_and_the_holding_company_feat._janis_joplin-bye_bye_baby_(alternate_take)_(bonus_track).flac"
#song = "/home/pi/Music/What_a-feeling.mp3"
songList = fc.getListOfFiles("") #"/home/pi/Music/What_a-feeling.mp3"
player = vlc.MediaPlayer(songList)

def elapsed_time(current, total, song):
    duration = total / 1000
    mm, ss   = divmod(duration, 60)
    elapsed = (current) / 1000
    mm2, ss2   = divmod(elapsed, 60)
    print ("Song : ", song, "%02d:%02d" % (mm,ss),"/", "%02d:%02d" % (mm2,ss2))

# play songs list or single music, repeat 0 = none, 1 = single, 2 = all
# random bool false = false, true = true
def play_SongList(songList, repeat, random):
    

#player = vlc.MediaPlayer("/home/pi/Music/What_a_feeling.mp3")
player.play()
time.sleep(1)
if(player.is_playing()):
    print("Total time {:}".format(player.get_length()))
while(player.is_playing()):
    elapsed_time(player.get_time(),player.get_length(), songList)
    time.sleep(1)
    #print("Remaining {:} | Total {:}".format(player.get_length() - player.get_time(),player.get_length()))
    
