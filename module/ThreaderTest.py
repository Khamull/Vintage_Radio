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
from subprocess import call
import MainDisplay as MD
import config as CF


def StartPigPIOD():
    call('sudo pigpiod', shell=True)

def rightWorkerCall(q):
    RW = RWorker.rWorker()
    RW.isRotation(q)
    RW.main()

def leftWorkerCall(q):
    LW = LWorker.lWorker()
    LW.isRotation(q)
    LW.main()

def leftClickCall(q):
    #print("leftClickCall")
    cl = LWorker.lWorker()
    cl.isClick(q)
    cl.main()

def rightClickCall(q):
    #print("leftClickCall")
    cr = RWorker.rWorker()
    cr.isClick(q)
    cr.main()


def RClickResult(qcl,qcol):
    #print("lClickResult")
    rd = RD.RotaryDigest()
    while True:
        #print("while")
        rd.clicksDigest(qcl,qcol)
        print("RC:",qcol.get())

 

def pRResult(q,qo):
    rd = RD.RotaryDigest()
    while True:
        rd.interval(q,qo)
        interval = qo.get()
        CF.interval = interval
        print("R:", interval)

def pLResult(q,qo):
    rd = RD.RotaryDigest()
    while True:
        rd.interval(q,qo)
        print("L:",qo.get())

def LClickResult(qcl,qcol):
    #print("lClickResult")
    rd = RD.RotaryDigest()
    while True:
        #print("while")
        rd.clicksDigest(qcl,qcol)
        print("LC:",qcol.get())

def mainDisplay():
    m = MD.Display()
    while True:
        m.main()
    
if __name__ == "__main__":
    StartPigPIOD()
    
    qr = Queue()
    ql = Queue()
    qor = Queue()
    qol = Queue()
    
    qcr = Queue()
    qcor = Queue()
    
    qcl = Queue()
    qcol = Queue()
    
    
    t1 = Thread(target = rightWorkerCall, args=(qr,))
    t2 = Thread(target = pRResult, args=(qr,qor))
    
    t3 = Thread(target = rightClickCall, args=(qcr,))
    t4 = Thread(target = RClickResult, args=(qcr,qcor))
    
    
    
    t5 = Thread(target = leftWorkerCall, args=(ql,))
    t6 = Thread(target = pLResult, args=(ql,qol))
    
    t7 = Thread(target = leftClickCall, args=(qcl,))
    t8 = Thread(target = LClickResult, args=(qcl,qcol))
    
    t9 = Thread(target = mainDisplay)
    
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    