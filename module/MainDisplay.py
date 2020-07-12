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
import Controll as ctrl
from time import sleep

#start the screen
# menu options if none is preseted are 1 - MP3(Internal) 2 - Bluetooth 3 - USB 4 - Settings
# time and date always displayed
# 4 - Settings Maybe basic volume, basic option to start up with, folder to music
# time settings as well(but this is just some basic ideas)
# and display the IP also!
# How to get to menu? Long press of volume button/
# navigate using Rotary+Press on option!

codes = CF.codes

def make_font(name, size):
    return D.make_font(name, size)

def menu_position(interval):
     lista = [0,0,0,0]
     if(interval >= 0 and interval <=25):
         lista[0] = 1
         #draw.rectangle((4, 14, 122, 24) , outline="white", fill="white")
         #draw.text((4, 14), "1 - Internal MP3", font=font,fill="black")
     if(interval >= 26 and interval <=50):
         lista[1] = 1
         #draw.rectangle((4, 26, 122, 36) , outline="white", fill="white")
         #draw.text((4, 26), "2 - Bluetooth", font=font,fill="black")
     if(interval >= 51 and interval <=75):
         lista[2] = 1
         #draw.rectangle((4, 38, 122, 49) , outline="white", fill="white")
         #draw.text((4, 38), "3 - USB", font=font,fill="black")
     if(interval >= 76 and interval <=100):
         lista[3] = 1
         #draw.rectangle((4, 51, 122, 62) , outline="white", fill="white")
         #draw.text((4, 50), "4 - Settings", font=font,fill="black")
     return lista
def Time():
    global today_date, today_time
    now = datetime.datetime.now()
    today_date = now.strftime("%d %b %y")
    today_time = now.strftime("%H:%M:%S")

def makeFonts(device):
    global font_basic, font_awesome, font_menu, font_basic_8, font_awesome_small
    font_basic = make_font("pixelmix.ttf", 10)
    font_basic_8 = make_font("pixelmix.ttf", 8)
    font_awesome = make_font("Font Awesome 5 Free-Solid-900.otf", device.height-48)
    font_awesome_small = make_font("Font Awesome 5 Free-Solid-900.otf", device.height-55)
    font_menu = make_font("Font Awesome 5 Free-Solid-900.otf", 13)

def updateMusic(c):
    c.get_music_info()

def updateTime(c):
    c.get_music_time()
        
def draw_menu():
    device = D.get_device()
    makeFonts(device)
    while CF.source == 1:    
        Time()
        with canvas(device) as draw:
            #basic outline Box and text rendered in portrait mode
            #draw.rectangle(device.bounding_box, outline="white", fill="black")
            D.draw_rectangle(draw, device)
            
            #date and time
            draw.line((0, 13, 128, 13), fill="white")
            draw.text((2, 1), today_date, fill="white")
            draw.text((78, 1), today_time, fill="white")
            #updateMusic()
            #ler controle de volume! Depois, ler primeito configuração inicial!
            p = menu_position(CF.interval)
            #musicInfo()
            #MP3
            if(p[0] == 1):
                draw.rectangle((4, 14, 122, 24) , outline="white", fill="white")
                draw.text((4, 14), "1 - Internal MP3", font=font_menu,fill="black")
            else:
                draw.text((4, 14), "1 - Internal MP3", font=font_menu,fill="white")
            #Bluetooth
            if(p[1] == 1):
                draw.rectangle((4, 26, 122, 36) , outline="white", fill="white")
                draw.text((4, 26), "2 - Bluetooth", font=font_menu,fill="black")
            else:
                draw.text((4, 26), "2 - Bluetooth", font=font_menu,fill="white")
            #USB
            if(p[2] == 1):
                draw.rectangle((4, 38, 122, 49) , outline="white", fill="white")
                draw.text((4, 38), "3 - USB", font=font_menu,fill="black")
            else:
                draw.text((4, 38), "3 - USB", font=font_menu,fill="white")
            #settings
            if(p[3] == 1):
                draw.rectangle((4, 51, 122, 62) , outline="white", fill="white")
                draw.text((4, 50), "4 - Settings", font=font_menu,fill="black")
            else:
                draw.text((4, 50), "4 - Settings", font=font_menu,fill="white")


def draw_player(c):
        device = D.get_device()
        makeFonts(device)
        while CF.source == 0:

            with canvas(device) as draw:
                #basic outline Box and text rendered in portrait mode
                #draw.rectangle(device.bounding_box, outline="white", fill="black")
                D.draw_rectangle(draw, device)
                Time()
                #date and time
                draw.line((0, 13, 128, 13), fill="white")
                draw.text((2, 1), today_date, fill="white")
                draw.text((78, 1), today_time, fill="white")
                #info = ctrl.get_music_info()
                #music name, artist and album(may be next music inline)
                updateMusic(c)
                updateTime(c)
                try:
                    draw.text(((device.width/4.3)- len(CF.music_info[0]), 14), CF.music_info[0]  , font=font_basic_8,fill="white")
                    draw.text(((device.width/3)- len(CF.music_info[1]), 22), CF.music_info[1]  , font=font_basic_8,fill="white")
                    draw.text(((device.width/3)- len(CF.time), 32), CF.time  , font=font_basic_8,fill="white")
                except:
                    pass
                
                #text position for music info(can be better) TODO: a Better Scroll 
                #c.get_music_info()
                #print(CF.music_info)
                
                volumetodisplay = str(CF.interval)+"%"
                volume = CF.interval
                #volume controls status info
                draw.text((25, 50), volumetodisplay, font=font_basic_8, fill="white")
                if volume > 1 and volume <= 50:
                    draw.text((5, 45), text=codes[2], font=font_awesome, fill="white")
                if volume > 51 and volume <=80:    
                    draw.text((5, 45), text=codes[0], font=font_awesome, fill="white")
                if volume > 80:           
                    draw.text((5, 45), text=codes[3], font=font_awesome, fill="white")
                if volume <= 0:
                    draw.text((5, 45), text=codes[1], font=font_awesome, fill="white")
                if CF.status == "play":
                    draw.text((110, 45), text=codes[5], font=font_awesome, fill="white")
                if CF.status == "pause":
                    draw.text((110, 45), text=codes[4], font=font_awesome, fill="white", contrast=10)
                if CF.second_status == "next":
                    draw.text((70, 45), text=codes[7], font=font_awesome, fill="white", contrast=10)
                if CF.second_status == "prev":
                    draw.text((70, 45), text=codes[6], font=font_awesome, fill="white", contrast=10)
                if CF.radom:
                    draw.text((50, 45), text=codes[8], font=font_awesome_small, fill="white", contrast=10)
                if CF.repeatAll:
                    draw.text((50, 53), text=codes[9], font=font_awesome_small, fill="white", contrast=10)
                if CF.repeatOne:
                    draw.text((50, 53), text=codes[10], font=font_awesome_small, fill="white", contrast=10)

def main():
    c = ctrl.CONTROLL()
    c.add_event_callbakcs()

    while True:
        if CF.source == 0:
            draw_player(c)
        if CF.source == 1:
            draw_menu()
    
    
    

        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass



