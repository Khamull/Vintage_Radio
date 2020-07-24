# -*- coding: utf-8 -*-
#source https://stackoverflow.com/questions/28440708/python-vlc-binding-playing-a-playlist

import vlc
import time
import os
import config as CF

class VLC:
    def __init__(self):
        self.Player = vlc.Instance('--loop')

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        if(CF.USBFolder == ""):
            path = CF.initFolder #r"C:\Users\dell5567\Desktop\engsong"
        else:
            path = CF.USBFolder
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
    
    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()
    def player_status(self):
        return self.listPlayer.is_playing()
    def set_playback_mode(self, mode):
        self.listPlayer.set_playback_mode(mode)
    def set_test(self):
        return self.Player.audio_output_list_get
    def get_music_title(self):
        return self.Player

def main():
    p = VLC()
    p.addPlaylist()
    p.play()
   
 

    
if __name__ == '__main__':
    main()   
