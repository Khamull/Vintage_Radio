#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:41:23 2021

Get's rotary queue and can return counter, position up or down, rotation position in circle grades

@author: Charles Path
"""
class RotaryDigest:
    def __init__(self):
        self.counter    = 0
        self.step       = 5
        self.max = 100
        self.min = 0

    def interval(self, q, qo):
        
        if q.get() == "1\n":
            if self.counter < self.max:
                self.counter += self.step
        else:
            if self.counter > self.min:
                if q.get() == "0\n":
                    self.counter -= self.step
        qo.put(self.counter)        
    
    