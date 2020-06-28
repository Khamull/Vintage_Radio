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
import MenuControll as MC
import config as CF
from time import sleep
import AudioPlayer as ap

#start the screen
# menu options if none is preseted are 1 - MP3(Internal) 2 - Bluetooth 3 - USB 4 - Settings
# time and date always displayed
# 4 - Settings Maybe basic volume, basic option to start up with, folder to music
# time settings as well(but this is just some basic ideas)
# and display the IP also!
# How to get to menu? Long press of volume button/
# navigate using Rotary+Press on oprion!

codes = ["\uf027", "\uf6a9", "\uf026", "\uf028", "\uf28b", "\uf144"]

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
    global font_basic, font_awesome, font_menu
    font_basic = make_font("pixelmix.ttf", 10)
    font_awesome = make_font("Font Awesome 5 Free-Solid-900.otf", device.height-40)
    font_menu = make_font("Font Awesome 5 Free-Solid-900.otf", 13)
        
def draw_menu():
    device = D.get_device()
    makeFonts(device)
    while True:    
        Time()
        with canvas(device) as draw:
            #basic outline Box and text rendered in portrait mode
            #draw.rectangle(device.bounding_box, outline="white", fill="black")
            D.draw_rectangle(draw, device)
            #date and time
            draw.line((0, 13, 128, 13), fill="white")
            draw.text((2, 1), today_date, fill="white")
            draw.text((78, 1), today_time, fill="white")
            
            #ler controle de volume! Depois, ler primeito configuração inicial!
            p = menu_position(CF.interval)
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

def draw_player():
        device = D.get_device()
        makeFonts(device)
        while True:

            with canvas(device) as draw:
                #basic outline Box and text rendered in portrait mode
                #draw.rectangle(device.bounding_box, outline="white", fill="black")
                D.draw_rectangle(draw, device)
                Time()
                #date and time
                draw.line((0, 13, 128, 13), fill="white")
                draw.text((2, 1), today_date, fill="white")
                draw.text((78, 1), today_time, fill="white")
                
                #music name, artist and album(may be next music inline)
                #draw.text((music_title_start - i, 13), music_info, font=font,fill="white")
                #draw.text((music_title_start - i, 23), next_music_info, font=font, fill="white")
                #text position for music info(can be better) TODO: a Better Scroll 

                volumetodisplay = str(CF.interval)+"%"
                volume = CF.interval
                #volume controls status info
                draw.text((37, 45), volumetodisplay, font=font_basic, fill="white")
                if volume > 0 and volume <= 40:
                    draw.text((5, 40), text=codes[2], font=font_awesome, fill="white")
                if volume > 40 and volume <=60:    
                    draw.text((5, 40), text=codes[0], font=font_awesome, fill="white")
                if volume > 60:           
                    draw.text((5, 40), text=codes[3], font=font_awesome, fill="white")
                if volume <= 0:
                    draw.text((5, 40), text=codes[1], font=font_awesome, fill="white")
                if CF.status == "play":
                    draw.text((100, 38), text=codes[5], font=font_awesome, fill="white")
                if CF.status == "pause":
                    draw.text((100, 38), text=codes[4], font=font_awesome, fill="white", contrast=10)
        
                #print(i)
                sleep(0.05)
    

def main():
    MC.main()
    draw_menu()    
    draw_player()    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass



