#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:00:15 2020
To turn the bluetooth on e off as we change of sources in the project
@author: Charles Path
"""

from subprocess import DEVNULL, STDOUT, check_call
from time import sleep
import config as cf

class BtControll:
        def __init__(self):
            self.on_command         = ['rfkill', 'unblock', 'bluetooth']
            self.off_command        = ['rfkill', 'block', 'bluetooth']
            self.off_discoverable    = ['sudo', 'hciconfig', 'hci0', 'pscan']
            self.on_discoverable    = ['sudo','hciconfig', 'hci0', 'piscan']
            self.bt_state   = 0
            self.disc_state   = 0
            
        def callBtCommands(self):
            self.runCommand()
        def runCommands(self):
            if self.bt_state == 0:
                print("ON")
                check_call(self.on_command, stdout=DEVNULL, stderr=STDOUT)
                self.bt_state = 1
            else:
                print("OFF")
                check_call(self.off_command, stdout=DEVNULL, stderr=STDOUT)               
                self.bt_state = 0
        
        def discCommands(self):
            self.changeDiscover()
        def changeDiscover(self):
            if self.disc_state == 0:
                print("Discoverable")
                check_call(self.on_discoverable, stdout=DEVNULL, stderr=STDOUT)
                self.disc_state = 1
            else:
                print("Undiscoverable")
                check_call(self.off_discoverable, stdout=DEVNULL, stderr=STDOUT)               
                self.disc_state = 0
        
        def offScan(self):
            print("Undiscoverable")
            self.commanRun(self.off_discoverable)
            self.disc_state = 0
        
        def onScan(self):
            print("Discoverable")
            self.commandRun(self.on_discoverable)
            self.disc_state = 1
        
        def onBt(self):
            print("ON")
            self.commandRun(self.on_command)
            self.bt_state = 1
        def offBt(self):
            print("OFF")
            self.commandRun(self.off_command)
            self.bt_state = 0
            
        
        def commandRun(self, command):
            check_call(command, stdout=DEVNULL, stderr=STDOUT) 
            self.updateState()
        
        def updateState(self):
            cf.btLastState = [self.bt_state, self.disc_state]    
            
        def main(self):
            self.discCommands()
            

if __name__ == '__main__':
    bt = BtControll()
    while True:
        bt.main()
        sleep(10)
    
