#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:41:23 2021

@author: Charles Path
"""
from pigpio_encoder.rotary import Rotary
from queue import Queue as Q
#qr = Q()

class lWorker:
    def __init__(self):
        self.ql = Q()
        self.qc = Q()

    def rotary_callback(self, counter):
        pass
        #print("Counter value: ", counter)
    
    def sw_short(self):
        self.qc.put("S")
        #print("Switch pressed")
    
    def sw_long(self):
        #global qr
        self.qc.put("L")
        #print("Switch long press")
    
    def up_callback(self, counter):
        #output("1 \n")
        #global qr
        self.ql.put("1\n")
        #print("Up rotation")
        #print("Counter value: ", counter)
    
    def down_callback(self, counter):
        #output("0 \n")
        #global qr
        self.ql.put("0\n")
        #print("Down rotation")
        #print("Counter value: ", counter)
    def isClick(self, q):
        self.qc = q
    
    def isRotation(self, q):
        self.ql = q
        
    def main(self):
        
        
        my_rotary = Rotary(clk_gpio=6, dt_gpio=26, sw_gpio=13)
        
        
        my_rotary.setup_rotary(min=0, max=100
                               , scale=5, debounce=200
                               , rotary_callback=self.rotary_callback
                               , up_callback=self.up_callback
                               , down_callback=self.down_callback)
        
        my_rotary.setup_switch(debounce=300
                               , long_press=True
                               , sw_short_callback=self.sw_short
                               , sw_long_callback=self.sw_long)
        #self.qr = q
        
        my_rotary.watch()

