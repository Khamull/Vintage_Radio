#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Charles Path using LUMA
# https://github.com/rm-hull/luma.examples/
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

#   The ideia is simple ply a given audio file
#   The commandas shoudl all be the same interface
#   The ability to navigate in folders and access specific
#   songs might be a good addon, also shuffle and repeat


from pygame import mixer #pygame mixer is garbage!

#initialize mixer
mixer.init()

#sound = mixer.Sound("/home/pi/Music/114-big_brother_and_the_holding_company_feat._janis_joplin-bye_bye_baby_(alternate_take)_(bonus_track).flac")
sound = mixer.Sound("/home/pi/Music/What_a_feeling.mp3")

try:
    while True:
        sound.play()
finally:
    sound.stop()