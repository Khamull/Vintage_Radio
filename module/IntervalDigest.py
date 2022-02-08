#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:32:20 2021

@author: Charles Path
"""

import config as CF
import time

############## To Get the Intervak from a Rotary and decide what to do #######################
############

#Increase Volume
#Change Menu Position
#LeftRightUp or Down
#Based on that, decide which function to call or which value to populate!

#I Will need a variable to tell where I am at the software, if music player(bt as well) 
#Will increase or decrease the audio
#If Menu, change the index position basedo on a new, 0 to 100 index
#If folder navigation, same as menu
#if game, then updownleftright based on the orientation(might add interval for limit of screen)
#Makes no differece which rotary Im using to move on menu screens, in music player mode, will have to do different acctions!
#while in Menu mode, interval will set same variabel!
#In music mode, one might do volume while other might do nextprevious

def Volume(interval):
    CF.interval = interval
    
def Status(statusID):
    if statusID == "1\n":
        CF.second_status = "next"
    if statusID == "0\n":
        CF.second_status = "prev"
    #Avaliate the end of the event next and play begin
    time.sleep(0.09)
    CF.second_status = ""
