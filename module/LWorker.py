#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pigpio_encoder.rotary import Rotary
import config as cf
import sys
from queue import Queue as Q
qr = Q()

def rotary_callback(counter):
    output("")
    #print("Counter value: ", counter)

def sw_short():
    global qr
    qr.put("s \n")
    #print("Switch pressed")

def sw_long():
    global qr
    qr.put("l \n")
    #print("Switch long press")

def up_callback(counter):
    #output("1 \n")
    global qr
    qr.put("1 \n")
    #print("Up rotation")
    #print("Counter value: ", counter)

def down_callback(counter):
    #output("0 \n")
    global qr
    qr.put("0 \n")
    #print("Down rotation")
    #print("Counter value: ", counter)

def output(output):
    sys.stdout.write(output)
    
def main(q):
    
    
    my_rotary = Rotary(clk_gpio=27, dt_gpio=22, sw_gpio=17)
    
    
    my_rotary.setup_rotary(min=0, max=100
                           , scale=5, debounce=200
                           , rotary_callback=rotary_callback
                           , up_callback=up_callback
                           , down_callback=down_callback)
    
    my_rotary.setup_switch(debounce=300
                           , long_press=True
                           , sw_short_callback=sw_short
                           , sw_long_callback=sw_long)
    global qr
    qr = q
    
    my_rotary.watch()

