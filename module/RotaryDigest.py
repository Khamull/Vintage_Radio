#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:41:23 2021

Get's rotary queue and can return counter, position up or down, rotation position in circle grades

@author: Charles Path
"""

import time

class RotaryDigest:
    def __init__(self):
        self.counter            = 0
        self.step               = 5
        self.max                = 100
        self.min                = 0
        self.timeout            = 0.5 # how long can pass between two clicks to consider them part of the same event
        self.short_click        = 0.65 # length of a single click
        self.long_click         = 1.0 # length of a long click
        self.very_long_click    = 4.0 # length of a veeeery long click
        self.clicks             = []
        

    def interval(self, q, qo):
        
        if q.get() == "1\n":
            if self.counter < self.max:
                self.counter += self.step
        else:
            if self.counter > self.min:
                if q.get() == "0\n":
                    self.counter -= self.step
        qo.put(self.counter)        
    
    #notsure, but we might need some calcs heres, will see when we got there!
    def hOrientation(self, q, qo):
        
        if q.get() == "1\n":
            qo.put("r")
        else:
            qo.put("l")
    
    def vOrientation(self, q, qo):
        if q.get() == "1\n":
            qo.put("u")
        else:
            qo.put("d") 
    #end of the might do come calcs
    
    #clicks from here on
    #count time between clicks and return the type
    def clicksDigest(self, q, qo):
        if q.get() == "S":
            qo.put("Short")
        else:
            qo.put("Long")
        #if q.get() == "S":
        #    qo.put("short")
        #else:
        #    qo.put("long")
    #count times for long clicks
    def longClikcs(self, q, qo):
        pass
    def calcTime():
        bTime = time.now
        pass
    