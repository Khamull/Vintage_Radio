#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:27:01 2021

@author: pi
"""

import RWorker, LWorker
from threading import Thread
from time import sleep
from queue import Queue

def rightWorkerCall(q):
    RWorker.main(q)

def leftWorkerCall(q):
    LWorker.main(q)

def pRResult(q):
    while True:
        print("R:", q.get())

def pLResult(q):
    while True:
        print("L:",q.get())

if __name__ == "__main__":
    qr = Queue()
    ql = Queue()
    t1 = Thread(target = rightWorkerCall, args=(qr,))
    t2 = Thread(target = leftWorkerCall, args=(ql,))
    t3 = Thread(target = pRResult, args=(qr,))
    t4 = Thread(target = pLResult, args=(ql,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()