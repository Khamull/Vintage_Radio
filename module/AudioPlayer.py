#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

#   The ideia is simple play a given audio file
#   The commands shoudl all be the same interface
#   The ability to navigate in folders and access specific
#   songs might be a good addon, also shuffle and repeat


import vlc
import FilesControll as fc
import config as cf
from time import sleep
import pygame as pg

def loadPlayer():
    songList = fc.getListOfFiles("")
    instance = vlc.Instance()
    player = instance.media_list_player_new()
    player.set_playback_mode(0)
    media_list = instance.media_list_new(songList)
    player.set_media_list(media_list)
    return player

def elapsed_time(current, total, title):
    try:
        duration = total / 1000
        mm, ss   = divmod(duration, 60)
        elapsed = (current) / 1000
        mm2, ss2   = divmod(elapsed, 60)
        time = "%02d:%02d" % (mm,ss),"/", "%02d:%02d" % (mm2,ss2)
        result = time[2]+time[1]+time[0]
        return result
    except:
        pass

def play(player):
    player.play()
    cf.status = "play"
def next(player):
    cf.second_status = "next"
    player.next()
    
def pause(player):
    cf.status = "pause"
    player.pause()
    
def previous(player):
    cf.second_status = "prev"
    player.previous()
    
def stop(player):
    cf.status = "stop"
    player.stop()
    
def player_status(player):
    return player.is_playing()

def music_info(player):
    try:
        list = [
                player.get_media_player().get_media().get_meta(0)   #music name
                ,player.get_media_player().get_media().get_meta(1)  #Artist
                ]
        return list
    except:
        pass
    # https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Meta-class.html
    #title = 0
    #artisit = 1
    #Genre = 2
    #Album = 3
    #TrackNumber = ""
    #TrackId = ""
    #   print(player.get_media_player().get_time())# will return path of current playing mp3 or mp4(sample from where I got the idea)    
    #   player.get_media_player().get_media().get_meta(0)
    #   gets different meta for display!
    
def music_track_time(player): 
    return elapsed_time(player.get_media_player().get_time(),player.get_media_player().get_length(), player.get_media_player().audio_get_track())

def playBackMode(player):
    if cf.repeatAll:
        player.set_playback_mode(vlc.PlaybackMode.default)
        cf.repeatAll = False
        cf.repeatOne = False
    if cf.repeatOne:
        player.set_playback_mode(vlc.PlaybackMode.loop)
        cf.repeatAll = False
        cf.repeatOne = True
    if not cf.repeatOne and not cf.repeatAll:
        player.set_playback_mode(vlc.PlaybackMode.repeat)
        cf.repeatAll = False
        cf.repeatOne = True

def main():
    p = loadPlayer()
    p.get_media_player().audio_set_delay(30)
    #sleep(5)
    play(p)
    
    
if __name__ == '__main__':
    main()  
    
    
