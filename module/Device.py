#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK


from __future__ import unicode_literals
from luma.core.interface.serial import spi
from luma.oled.device import ssd1309
from PIL import ImageFont
import os

def get_device():
    # rev.1 users set port=0
    # substitute spi(device=0, port=0) below if using that interface
    serial = spi(device=0, port=0, cs_high=True)#cs_high = True is a workaround to this isseu https://github.com/raspberrypi/linux/issues/3355
    #s erial = spi(device=0, port=0)
    # substitute ssd1331(...) or sh1106(...) below if using that device
    device = ssd1309(serial)
    return device

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    #print(font_path)
    return ImageFont.truetype(font_path, size)

def draw_rectangle(draw, device):
    draw.rectangle(device.bounding_box, outline="white", fill="black")

