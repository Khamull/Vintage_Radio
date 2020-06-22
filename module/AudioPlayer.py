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
import FilesControll as fc
import time

def loadPlayer():
    songList = fc.getListOfFiles("")
    instance = vlc.Instance()
    player = instance.media_list_player_new()
    player.set_playback_mode(0)
    media_list = instance.media_list_new(songList)
    player.set_media_list(media_list)
    return player

def elapsed_time(current, total, title):
    duration = total / 1000
    mm, ss   = divmod(duration, 60)
    elapsed = (current) / 1000
    mm2, ss2   = divmod(elapsed, 60)
    print (title, "- %02d:%02d" % (mm,ss),"/", "%02d:%02d" % (mm2,ss2))

def play(player):
    player.play()
def next(player):
    player.next()
def pause(player):
    player.pause()
def previous(player):
    player.previous()
def stop(player):
    player.stop()
def player_status(player):
    return player.is_playing()

def music_info(player):
    #title = 0
    #artisit = 1
    #Genre = 2
    #Album = 3
    #TrackNumber = ""
    #TrackId = ""
    #    print(player.get_media_player().get_time())# will return path of current playing mp3 or mp4(sample from where I got the idea)    
    #gets different meta for display!
    player.get_media_player().get_media().get_meta(0)
    
def music_track_time(player): 
    return elapsed_time(player.get_media_player().get_time(),player.get_media_player().get_length(), player.get_media_player().audio_get_track())
def main():
    player = loadPlayer()
    play(player)
    time.sleep(10)
    pause(player)
    time.sleep(10)
    play(player)
    time.sleep(10)
    next(player)
    time.sleep(10)
    previous(player)
    time.sleep(10)
    
if __name__ == '__main__':
    main()  
    
    
