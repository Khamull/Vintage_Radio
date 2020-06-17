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

#start the screen
# menu options if none is preseted are 1 - MP3(Internal) 2 - Bluetooth 3 - USB 4 - Settings
# time and date always displayed
# 4 - Settings Maybe basic volume, basic option to start up with, folder to music
# time settings as well(but this is just some basic ideas)
# and display the IP also!
# How to get to menu? Long press of volume button/
# navigate using Rotary+Press on oprion!

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
        
def draw_menu():
    device = D.get_device()
    font = make_font("Font Awesome 5 Free-Solid-900.otf", 13)
    while True:    
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
      
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
                draw.text((4, 14), "1 - Internal MP3", font=font,fill="black")
            else:
                draw.text((4, 14), "1 - Internal MP3", font=font,fill="white")
            #Bluetooth
            if(p[1] == 1):
                draw.rectangle((4, 26, 122, 36) , outline="white", fill="white")
                draw.text((4, 26), "2 - Bluetooth", font=font,fill="black")
            else:
                draw.text((4, 26), "2 - Bluetooth", font=font,fill="white")
            #USB
            if(p[2] == 1):
                draw.rectangle((4, 38, 122, 49) , outline="white", fill="white")
                draw.text((4, 38), "3 - USB", font=font,fill="black")
            else:
                draw.text((4, 38), "3 - USB", font=font,fill="white")
            #settings
            if(p[3] == 1):
                draw.rectangle((4, 51, 122, 62) , outline="white", fill="white")
                draw.text((4, 50), "4 - Settings", font=font,fill="black")
            else:
                draw.text((4, 50), "4 - Settings", font=font,fill="white")
def main():
    MC.main()
    draw_menu()    
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass



