#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:11:05 2020

@author: Charles Path
"""
from RPi import GPIO
from threading import Thread
import time
from time import sleep
import config as cf
import MainDisplay as m
import Controll as C
import AudioPlayer as ap
import FilesControll as fc

class Click:
    def __init__(self):
        self.l_btn    = cf.l_btn
        self.clicks    = cf.clicks
        self.timeout = 0.5 # how long can pass between two clicks to consider them part of the same event
        self.short_click = 0.65 # length of a single click
        self.long_click = 1.0 # length of a long click
        self.very_long_click = 4.0 # length of a veeeery long click
        self.display = m.Display()
        self.controll = C.CONTROLL()
        self.GPIO_setup()
        
        self.controll.get_player()
        self.controll.add_event_callbakcs()
        self.vlc_player = self.controll.vlc_player
        ap.play(self.vlc_player)
        
        
    
    def GPIO_setup(self):
        #GPIO SETUP
        GPIO.setmode(GPIO.BCM)
        #left controll
        GPIO.setup(self.l_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def pressed(self):
        start_time = time.time()
        while not GPIO.input(self.l_btn):
            time.sleep(.1)
        pressed_time = time.time() - start_time
        if pressed_time < self.short_click:
            return 'short'
        elif pressed_time > self.very_long_click:
            return 'very long'
        else:
            return 'long'

    # returns the kind of click event
    def pressing(self):
    
        tmpclicks = []
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            if not GPIO.input(self.l_btn):
                tmpclicks.append(self.pressed())
                start_time = time.time()
        self.clicks = tmpclicks
    
    def readClick(self):
        while True:
            if cf.source == 0 or cf.source == 3:
                self.controll.get_music_info()
                self.controll.get_music_time()
            self.display.main()#go figure, here it works, but all around, it does not!
            try:
                t

            except NameError:
                if not GPIO.input(self.l_btn):
                    t= Thread(target=self.pressing)
                    t.start()
            else:
                clicks = self.clicks
                if clicks:
                    if clicks == ['short']:
                        
                        print ("Single click")
                        if cf.source == 0 or cf.source == 3:
                            self.controll.button_callback()
                        
                        elif cf.source == 5:
                            cf.folderSelected = cf.interval
                            self.controll.reloadPlayer()
                            #cf.lastVolume = cf.interval
                            cf.source = 0
                            self.controll.checkNavigationSource(False)
                        else:
                            self.controll.menu_control()
                    elif clicks == ['short', 'short']:
                        self.controll.checkNavigationSource(False)
                        print ("Double click")
                        #playback mode
                        self.changePlayBackMode()
                        #print(cf.interval)
                    elif clicks == ['short','short', 'short']:
                        print ("Triple click")
                        self.controll.RandomPlayList()
                    elif clicks == ['long']:
                        print ("Long click")
                    elif clicks == ['long', 'long']:
                        print ("Double long click")
                        self.controll.checkNavigationSource(False)
                        if cf.source == 0 or cf.source == 3:
                            cf.lastVolume = cf.interval
                            cf.lastOption = cf.source
                        cf.source = 1
                        cf.interval = 0
                        self.controll.interval = 0
                    elif clicks == ['very long']:
                        print ("Very long click")
                        cf.lastVolume = cf.interval
                        cf.lastOption = cf.source
                        if cf.source == 3:
                            fc._getListOfFolders(cf.USBFolder)
                        else:
                            fc._getListOfFolders(cf.initFolder)
                        self.controll.checkNavigationSource(True)
                        sleep(0.1)
                        cf.source = 5
                        
                        
                    self.clicks = []
                    del t
    
    def changePlayBackMode(self):
        cf.playbackMode = self.controll.changePlayBackMode()
    def main(self):
        self.readClick()
        #t1 = Thread(target = self.readClick())
        #t1.setDaemon(True)
        #t1.start()

if __name__ == "__main__":
    c = Click()
    c.main()    

    
        
        
