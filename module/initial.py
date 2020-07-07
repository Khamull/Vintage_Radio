# -*- coding: utf-8 -*-

import AudioPlayer as ap
import MainDisplay as mp
import Controll as con
import config as cf
import asyncio
from time import sleep

def startControll():
   con.main()

def main():
    if cf.defaultStart == 0:
        asyncio.run(mp.draw_player())
    else:
        mp.draw_menu()
    sleep(1)
    startControll()
if __name__ == '__main__':
    main() 
