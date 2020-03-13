# -*- coding: utf-8 -*-
import DisplayTemplate as DT
import config as cf
from time import sleep
import multiprocess as mp
mp.process(DT.main())
i = 0 
while True:
    
    cf.volume = i
    print(cf.volume)
    DT.update_volume()
    sleep(1)
    i+=1
#    DT.update_volume()
#    sleep(5)
#    DT.update_volume()
#    sleep(5)
#    DT.update_volume(70)
#    sleep(5)
#    DT.update_volume(50)
#    sleep(5)
#    DT.update_volume(40)
#    sleep(5)
#    DT.update_volume(30)
#    sleep(5)
#    DT.update_volume(20)
#    sleep(5)
#    DT.update_volume(10)
#    sleep(5)
#    DT.update_volume(1)
#    sleep(5)
#    DT.update_volume(0)
#    sleep(5)
#
#
#
