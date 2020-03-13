#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK


from __future__ import unicode_literals
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from time import sleep
import datetime
import os
import sys
from luma.core.virtual import viewport

from PIL import ImageFont
#volume low, mute, Volume Low, Volume High, Pause, Play
codes = ["\uf027", "\uf6a9", "\uf026", "\uf028", "\uf28b", "\uf144"]
def get_device():
    # rev.1 users set port=0
    # substitute spi(device=0, port=0) below if using that interface
    serial = spi(device=0, port=0)
    # substitute ssd1331(...) or sh1106(...) below if using that device
    device = ssd1309(serial)
    return device

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    print(font_path)
    return ImageFont.truetype(font_path, size)

def main():
    #defining the device we are using
    device = get_device()
    #testing with variable for the scroll effect want
    music_title_start = 5
    music_info = "Music - music_name -" + " Music Artist - music_artist "
    mlen = len(music_info)
    index = (device.width/mlen)*100

    next_music_info = "Next Playing = music_name"
    i = 0
    j = 0
    z = 0
    #defining font types to use in different parts of the screen
    font = make_font("pixelmix.ttf", 10)
    font_awesome = make_font("fontawesome-webfont.ttf", device.height - 35)
    
    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        with canvas(device) as draw:
            
            #basic outline Box and text rendered in portrait mode
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            
            #date and time
            draw.line((0, 13, 128, 13), fill="white")
            draw.text((2, 1), today_date, fill="white")
            draw.text((78, 1), today_time, fill="white")
            
            #music name, artist and album(may be next music inline)
            draw.text((music_title_start - i, 13), music_info, font=font,fill="white")
            draw.text((music_title_start - i, 23), next_music_info, font=font, fill="white")
            #text position for music info(can be better) TODO: a Better Scroll 
            i+= 1
            if i >= index:
                music_title_start = 5
                i = 0
            
            #volume controls status info
            draw.text((5, 33), text=codes[0], font=font_awesome, fill="white")
            draw.text((25, 33), text=codes[1], font=font_awesome, fill="white")
            draw.text((45, 33), text=codes[2], font=font_awesome, fill="white")
            draw.text((65, 33), text=codes[3], font=font_awesome, fill="white")
            draw.text((85, 33), text=codes[4], font=font_awesome, fill="white")
            draw.text((105, 33), text=codes[5], font=font_awesome, fill="white", contrast=10)
            
            
            
            #print(i)
            sleep(0.05)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
