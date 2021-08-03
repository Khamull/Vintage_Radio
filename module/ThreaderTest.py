#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:27:01 2021

@author: Charles Path
"""

import RWorker, LWorker
import RotaryDigest as RD
from threading import Thread
from queue import Queue

def rightWorkerCall(q):
    RWorker.main(q)

def leftWorkerCall(q):
    LWorker.main(q)

def pRResult(q,qo):
    rd = RD.RotaryDigest()
    while True:
        rd.interval(q,qo)
        print("R:", qo.get())

def pLResult(q,qo):
    rd = RD.RotaryDigest()
    while True:
        rd.interval(q,qo)
        print("L:",qo.get())
        
if __name__ == "__main__":
    
    qr = Queue()
    ql = Queue()
    qor = Queue()
    qol = Queue()
    
    t1 = Thread(target = rightWorkerCall, args=(qr,))
    t2 = Thread(target = leftWorkerCall, args=(ql,))
    
    t3 = Thread(target = pRResult, args=(qr,qor))
    t4 = Thread(target = pLResult, args=(ql,qol))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()