#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

from __future__ import unicode_literals
from luma.core.render import canvas
import datetime
import Device as D
import config as CF

#start the screen
# menu options if none is preseted are 1 - MP3(Internal) 2 - Bluetooth 3 - USB 4 - Settings
# time and date always displayed
# 4 - Settings Maybe basic volume, basic option to start up with, folder to music
# time settings as well(but this is just some basic ideas)
# and display the IP also!
# How to get to menu? Long press of volume button/
# navigate using Rotary+Press on option!

class Display:
    def __init__(self):
        self.codes              = CF.codes
        self.today_date         = None
        self.today_time         = None
        self.device             = D.get_device()
        self.font_basic         = None
        self.font_basic_8       = None
        self.font_awesome       = None
        self.font_awesome_small = None
        self.font_menu          = None
        self.interval = CF.interval
        self.source = CF.source
        
        self.makeFonts(self.device)
        
    def make_font(self, name, size):
        return D.make_font(name, size)

    def menu_position(self):
         list = [0,0,0,0]
         self.interval = CF.interval
         if(self.interval >= 0 and self.interval <=25):
             list[0] = 1
             #draw.rectangle((4, 14, 122, 24) , outline="white", fill="white")
             #draw.text((4, 14), "1 - Internal MP3", font=font,fill="black")
         if(self.interval >= 26 and self.interval <=50):
             list[1] = 1
             #draw.rectangle((4, 26, 122, 36) , outline="white", fill="white")
             #draw.text((4, 26), "2 - Bluetooth", font=font,fill="black")
         if(self.interval >= 51 and self.interval <=75):
             list[2] = 1
             #draw.rectangle((4, 38, 122, 49) , outline="white", fill="white")
             #draw.text((4, 38), "3 - USB", font=font,fill="black")
         if(self.interval >= 76 and self.interval <=100):
             list[3] = 1
             #draw.rectangle((4, 51, 122, 62) , outline="white", fill="white")
             #draw.text((4, 50), "4 - Settings", font=font,fill="black")
         return list
    def Time(self):
        now = datetime.datetime.now()
        self.today_date = now.strftime("%d %b %y")
        self.today_time = now.strftime("%H:%M:%S")

    def makeFonts(self, device):
        self.font_basic          = self.make_font("pixelmix.ttf", 10)
        self.font_basic_8        = self.make_font("pixelmix.ttf", 8)
        #Font Awesome 5 Brands-Regular-400.otf
        #self.font_awesome        = self.make_font("Font Awesome 5 Free-Solid-900.otf", device.height-48)
        #self.font_awesome_small  = self.make_font("Font Awesome 5 Free-Solid-900.otf", device.height-55)
        self.font_awesome        = self.make_font("Font Awesome 5 Free-Solid-900.otf", device.height-48)
        self.font_awesome_small  = self.make_font("Font Awesome 5 Free-Solid-900.otf", device.height-55)
        self.font_menu           = self.make_font("Font Awesome 5 Free-Solid-900.otf", 13)

    def draw_bluetooth(self):
        #while CF.source == 1:    
            self.Time()
            with canvas(self.device) as draw:
                #basic outline Box and text rendered in portrait mode
                #draw.rectangle(device.bounding_box, outline="white", fill="black")
                D.draw_rectangle(draw, self.device)
                
                #date and time
                draw.line((0, 13, 128, 13), fill="white")
                draw.text((2, 1), self.today_date, fill="white")
                draw.text((78, 1), self.today_time, fill="white")
                draw.text((15, 14), "Bluetooth" , font=self.font_basic_8,fill="white")
                
    def draw_boat(self):
    #while CF.source == 1:    
        self.Time()
        with canvas(self.device) as draw:
            #basic outline Box and text rendered in portrait mode
            #draw.rectangle(device.bounding_box, outline="white", fill="black")
            D.draw_rectangle(draw, self.device)
            
            #date and time
            draw.line((0, 13, 128, 13), fill="white")
            draw.text((2, 1), self.today_date, fill="white")
            draw.text((78, 1), self.today_time, fill="white")
            draw.text((15, 14), "Folder Navigation" , font=self.font_basic_8,fill="white")
            try:
                draw.rectangle((9, 32, 122, 24) , outline="white", fill="white")
                draw.text((10, 24), CF.listDirectoriesSelect[CF.interval] , font=self.font_basic_8,fill="black")
                draw.text((10, 34), CF.listDirectoriesSelect[CF.interval+1] , font=self.font_basic_8,fill="white")
                draw.text((10, 44), CF.listDirectoriesSelect[CF.interval+2] , font=self.font_basic_8,fill="white")
                draw.text((10, 54), CF.listDirectoriesSelect[CF.interval+3] , font=self.font_basic_8,fill="white")
            except:
                pass
            
            
    def draw_settings(self):
    #while CF.source == 1:    
        self.Time()
        with canvas(self.device) as draw:
            #basic outline Box and text rendered in portrait mode
            #draw.rectangle(device.bounding_box, outline="white", fill="black")
            D.draw_rectangle(draw, self.device)
            
            #date and time
            draw.line((0, 13, 128, 13), fill="white")
            draw.text((2, 1), self.today_date, fill="white")
            draw.text((78, 1), self.today_time, fill="white")
            draw.text((15, 14), "Settings" , font=self.font_basic_8,fill="white")
            
       
    def draw_menu(self):
        #while CF.source == 1:    
            self.Time()
            with canvas(self.device) as draw:
                #basic outline Box and text rendered in portrait mode
                #draw.rectangle(device.bounding_box, outline="white", fill="black")
                D.draw_rectangle(draw, self.device)
                
                #date and time
                draw.line((0, 13, 128, 13), fill="white")
                draw.text((2, 1), self.today_date, fill="white")
                draw.text((78, 1), self.today_time, fill="white")
                #updateMusic()
                #ler controle de volume! Depois, ler primeito configuração inicial!
                p = self.menu_position()
                #musicInfo()
                #MP3
                if(p[0] == 1):
                    draw.rectangle((4, 14, 122, 24) , outline="white", fill="white")
                    draw.text((4, 14), "1 - Internal MP3", font=self.font_menu,fill="black")
                else:
                    draw.text((4, 14), "1 - Internal MP3", font=self.font_menu,fill="white")
                #Bluetooth
                if(p[1] == 1):
                    draw.rectangle((4, 26, 122, 36) , outline="white", fill="white")
                    draw.text((4, 26), "2 - Bluetooth", font=self.font_menu,fill="black")
                else:
                    draw.text((4, 26), "2 - Bluetooth", font=self.font_menu,fill="white")
                #USB
                if(p[2] == 1):
                    draw.rectangle((4, 38, 122, 49) , outline="white", fill="white")
                    draw.text((4, 38), "3 - USB", font=self.font_menu,fill="black")
                else:
                    draw.text((4, 38), "3 - USB", font=self.font_menu,fill="white")
                #settings
                if(p[3] == 1):
                    draw.rectangle((4, 51, 122, 62) , outline="white", fill="white")
                    draw.text((4, 50), "4 - Settings", font=self.font_menu,fill="black")
                else:
                    draw.text((4, 50), "4 - Settings", font=self.font_menu,fill="white")


    def draw_player(self):
            #while True:
                
                with canvas(self.device) as draw:
                    #basic outline Box and text rendered in portrait mode
                    #draw.rectangle(device.bounding_box, outline="white", fill="black")
                    D.draw_rectangle(draw, self.device)
                    self.Time()
                    #date and time
                    draw.line((0, 13, 128, 13), fill="white")
                    draw.text((2, 1), self.today_date, fill="white")
                    draw.text((78, 1), self.today_time, fill="white")
                    #info = ctrl.get_music_info()
                    #music name, artist and album(may be next music inline)
                    if(CF.message):
                        draw.text((25, 14), CF.message  , font=self.font_basic_8,fill="white")
                    else:
                        try:
                            draw.text(((self.device.width/4.3)- len(CF.music_info[0]), 14), CF.music_info[0]  , font=self.font_basic_8,fill="white")
                            draw.text(((self.device.width/3)- len(CF.music_info[1]), 22), CF.music_info[1]  , font=self.font_basic_8,fill="white")
                            draw.text(((self.device.width/3)- len(CF.time), 32), CF.time  , font=self.font_basic_8,fill="white")
                        except:
                            pass
                    
                    #text position for music info(can be better) TODO: a Better Scroll 
                    #c.get_music_info()
                    #print(CF.music_info)
                    
                    volumetodisplay = str(CF.interval)+"%"
                    #print(volumetodisplay)
                    volume = CF.interval
                    
                    #volume controls status info
                    draw.text((25, 50), volumetodisplay, font=self.font_basic_8, fill="white")
                    if volume > 1 and volume <= 50:
                        draw.text((5, 45), text=self.codes[2], font=self.font_awesome, fill="white")
                    if volume > 51 and volume <=80:    
                        draw.text((5, 45), text=self.codes[0], font=self.font_awesome, fill="white")
                    if volume > 80:           
                        draw.text((5, 45), text=self.codes[3], font=self.font_awesome, fill="white")
                    if volume <= 0:
                        draw.text((5, 45), text=self.codes[1], font=self.font_awesome, fill="white")
                    if CF.status == "play":
                        draw.text((110, 45), text=self.codes[5], font=self.font_awesome, fill="white")
                    if CF.status == "pause":
                        draw.text((110, 45), text=self.codes[4], font=self.font_awesome, fill="white", contrast=10)
                    if CF.second_status == "next":
                        draw.text((80, 45), text=self.codes[7], font=self.font_awesome, fill="white", contrast=10)
                    if CF.second_status == "prev":
                        draw.text((80, 45), text=self.codes[6], font=self.font_awesome, fill="white", contrast=10)
                    if CF.random:
                        draw.text((50, 45), text=self.codes[8], font=self.font_awesome_small, fill="white", contrast=10)
                    if CF.playbackMode == 1:
                        draw.text((50, 53), text=self.codes[9], font=self.font_awesome_small, fill="white", contrast=10)
                    if CF.playbackMode == 2:
                        draw.text((50, 53), text=self.codes[10], font=self.font_awesome_small, fill="white", contrast=10)
                    if CF.playbackMode == 0:
                        draw.text((50, 53), text="", font=self.font_awesome_small, fill="white", contrast=10)
                    if CF.source == 3:
                        draw.text((65, 53), text=self.codes[11], font=self.font_awesome_small, fill="white", contrast=10)
                    if CF.source == 0:
                        draw.text((65, 53), text=self.codes[12], font=self.font_awesome_small, fill="white", contrast=10)

    def main(self):
        if CF.source == 0 or CF.source == 3:
            self.draw_player()
        if CF.source == 1:
            self.draw_menu()
        if CF.source == 2:
            self.draw_bluetooth()
        if CF.source == 4:
            self.draw_settings()
        if CF.source == 5:
            self.draw_boat()


if __name__ == "__main__":
    try:
        m = Display()
        m.main()
    except KeyboardInterrupt:
        pass



