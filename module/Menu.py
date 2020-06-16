#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK


from __future__ import unicode_literals
from luma.core.render import canvas
from time import sleep
import datetime
import os
import config as cf
import Device as D

#start the screen
# menu options if none is preseted are 1 - MP3(Internal) 2 - Bluetooth 3 - USB 4 - Settings
# time and date always displayed
# 4 - Settings Maybe basic volume, basic option to start up with, folder to music
# time settings as well(but this is just some basic ideas)
# and display the IP also!
# How to get to menu? Long press of volume button/
# navigate using Rotary+Press on oprion!

def get_device():
    device = D.get_device()
    return device



