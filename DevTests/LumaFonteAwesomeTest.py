#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

from __future__ import unicode_literals

"""
A wander through some of the font awesome
TTF glyphs.

See: http://fontawesome.io/license/ for license details of included
fontawesome-webfont.ttf file
"""

import os
import sys
import random
from PIL import ImageFont

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from time import sleep
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator

codes = ["\uf027", "\uf6a9", "\uf026", "\uf028"]

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), name))
    print(font_path)
    return ImageFont.truetype(font_path, size)

def main():
    # rev.1 users set port=0
    # substitute spi(device=0, port=0) below if using that interface
    serial = spi(device=0, port=0)
    # substitute ssd1331(...) or sh1106(...) below if using that device
    device = ssd1309(serial)
    font = make_font("fontawesome-webfont.ttf", device.height - 10)
    with canvas(device) as draw:
        w, h = draw.textsize("\uf027", font=font)
        left = (device.width - 50) / 2
        top = (device.height - 50) / 2
        draw.text((left, top), "\uf027", font=font, fill="white")
        
        print(f"left: {left}, top: {top}")
    
    with canvas(device) as draw:
        w, h = draw.textsize("\uf027", font=font)
        left = (device.width - w) / 2
        top = (device.height - h) / 2
        draw.text((left, top), "\uf028", font=font, fill="white")
        
        print(f"left: {left}, top: {top}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass