#!/usr/bin/python3
from RPi import GPIO
import config as cf
from subprocess import DEVNULL, STDOUT, check_call

class CONTROLL:
    def __init__(self):
        self.Mode   = cf.source
        self.clk    = cf.l_clk
        self.dt     = cf.l_dt
        self.btn    = cf.l_btn
        self.step   = cf.step
        self.preInterval = self.interval = cf.interval
        self.min = cf.min
        self.max = cf.max
        self.isReseted = False
        self.GPIO_setup()
        self.states_setup()
    
    def GPIO_setup(self):
        #GPIO SETUP
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def states_setup(self):
        self.clkLastState = GPIO.input(self.clk)
        self.btnLastState = GPIO.input(self.btn)
 
    def add_event_callbakcs(self):
        print("GPIO event add called")
        GPIO.add_event_detect(self.btn,GPIO.RISING,callback=self.button_callback, bouncetime=300)
        GPIO.add_event_detect(self.clk,GPIO.FALLING,callback=self.interval_calc,bouncetime=4) 
        
    
    def interval_calc(self, channel):
        clkState = GPIO.input(self.clk)
        dtState = GPIO.input(self.dt)
        if clkState != self.clkLastState:
            if self.isReseted:
                self.isReseted = False
                self.interval = 0
            if dtState != clkState:
                self.interval += self.step
                if self.interval > self.max:
                    self.interval = self.max
                cf.interval = self.interval
                print(self.interval)
            else:
                self.interval -= self.step
                if self.interval < self.min:
                    self.interval = self.min
                cf.interval = self.interval
                print(self.interval)
        self.clkLastState = clkState
        #At the end check the current source and do the needed
        if cf.source == 0:
            self.set_volume()
        
    
    def set_volume(self):
        command = ["amixer", "cset", "numid=3", "{}%".format(cf.interval)]
        check_call(command, stdout=DEVNULL, stderr=STDOUT)
    
    def get_volume(self):
        command = ["amixer", "sget", "Master", "| awk -F'[][]' '{print $2}'"]
        self.interval = check_call(command, stdout=DEVNULL, stderr=STDOUT)
    
    def volume_state(self):
        volume = self.interval
        if self.isReseted:
            volume          = cf.lastVolume
            self.interval   = cf.lastVolume
            cf.interval     = cf.lastVolume
            self.isReseted = False
            print("Unmuted")
        else:
            cf.lastVolume = volume
            volume = 0
            self.isReseted = True
            cf.interval = volume
            self.interval = volume
            print("Muted")
        self.set_volume()
    
    
        
    def button_callback(self, channel):
        print("Button Call Back")
        if cf.source == 0:
           #controls volume mute/unmute
           self.volume_state()
        if cf.source == 1:
            #gets the current selected menu option
           self.menu_control()
        if cf.source == 2:
            #gets the current selected menu option
           self.menu_control()
        if cf.source == 3:
            #gets the current selected menu option
           self.menu_control()
        
    def menu_control(self):
        if(self.interval >= 0 and self.interval <=25): 
            cf.source = 0
            print("Selected option 1")
        if(self.interval >= 26 and self.interval <=50):
            cf.source = 1
            print("Selected option 2")
        if(self.interval >= 51 and self.interval <=75):
            cf.source = 2
            print("Selected option 3")
        if(self.interval >= 76 and self.interval <=100):
            cf.source = 3
            print("Selected option 4")

def main():
    #print(interval)
    c = CONTROLL()
    c.add_event_callbakcs()


if __name__ == '__main__':
    print("main init")
    main()

