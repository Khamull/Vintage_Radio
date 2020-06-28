#!/usr/bin/python3
from RPi import GPIO
import config as cf
from subprocess import DEVNULL, STDOUT, check_call

class CONTROLL:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.Mode   = cf.source
        self.clk    = cf.l_clk
        self.dt     = cf.l_dt
        self.btn    = cf.l_btn
        self.step   = cf.step
        self.preInterval = self.interval = cf.interval
        self.isReseted = False
        
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.clkLastState = GPIO.input(self.clk)
        self.btnLastState = GPIO.input(self.btn)
        
        print(self.clk)
        print(self.dt)
        print(self.btn)
        #self.GPIO_setup()
        #GPIO.add_event_detect(self.clk,GPIO.FALLING,callback=self.interval_calc,bouncetime=4) 
    
    def GPIO_setup(self):
        #GPIO SETUP
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.clkLastState = GPIO.input(self.clk)
        self.btnLastState = GPIO.input(self.btn)
 
    def add_event_callbakcs(self):
        print("GPIO event add called")
        GPIO.add_event_detect(self.btn,GPIO.RISING,callback=self.button_callback, bouncetime=300)
        GPIO.add_event_detect(self.clk,GPIO.FALLING,callback=self.interval_calc,bouncetime=4) 
        
    
    def interval_calc(self, channel):
        #global preInterval, interval, isReseted, clkLastState, interval
        clkState = GPIO.input(self.clk)
        print(clkState)
        dtState = GPIO.input(self.dt)
        print(dtState)
        if clkState != self.clkLastState:
            if self.isReseted:
                self.isReseted = False
                self.interval = 0
            if dtState != clkState:
                self.interval += self.step
                if self.interval > max:
                    self.interval = max
                cf.interval = self.interval
                print(self.interval)
            else:
                self.interval -= self.step
                if self.interval < min:
                    self.interval = min
                cf.interval = self.interval
                print(self.interval)
        self.interval = self.interval
        self.clkLastState = clkState
    
    def button_callback(self, channel):
        if cf.source == 0:
           #gets the current selected menu option
           self.menu_control(self)
        if cf.source == 1:
           #controls volume mute/unmute
           print("Mute or Unmute")
        
    def menu_control(self):
        if(self.interval >= 0 and self.interval <=25):
            print("Selected option 1")
        if(self.interval >= 26 and self.interval <=50):
            print("Selected option 2")
        if(self.interval >= 51 and self.interval <=75):
            print("Selected option 3")
        if(self.interval >= 76 and self.interval <=100):
            print("Selected option 4")
        self.btnLastState = self.btnPushed
    



#clk = 22
#dt = 27
#btn = 17
#
## vals from output of amixer cget numid=1
#min = 0
#max = 100
#step = 10
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
#
#clkLastState = GPIO.input(clk)
#btnLastState = GPIO.input(btn)
#interval = 0
#
#isReseted = False
#preInterval = interval = cf.interval # give it some interval to start with
#
#
#def option_callback(channel):
#    global preInterval, interval, isReseted, clkLastState, interval
#    clkState = GPIO.input(clk)
#    dtState = GPIO.input(dt)
#    if clkState != clkLastState:
#        if isReseted:
#            isReseted = False
#            interval = 0
#        if dtState != clkState:
#            interval += step
#            if interval > max:
#                interval = max
#            cf.interval = interval
#            print(interval)
#        else:
#            interval -= step
#            if interval < min:
#                interval = min
#            cf.interval = interval
#            print(interval)
#        print(interval)
#    interval = interval
#    clkLastState = clkState
#
#def button_callback(channel):
#    global btnLastState
#    global interval
#    btnPushed = GPIO.input(btn)
#    if(interval >= 0 and interval <=25):
#        print("Selected option 1")
#    if(interval >= 26 and interval <=50):
#        print("Selected option 2")
#    if(interval >= 51 and interval <=75):
#        print("Selected option 3")
#    if(interval >= 76 and interval <=100):
#        print("Selected option 4")
#    btnLastState = btnPushed
#
##adding event listener for click
#GPIO.add_event_detect(btn,GPIO.RISING,callback=button_callback, bouncetime=300)
##listening for a input to be able to mesure both!
#GPIO.add_event_detect(clk,GPIO.FALLING,callback=option_callback,bouncetime=4)   

def main():
    #print(interval)
    c = CONTROLL()
    c.add_event_callbakcs()

if __name__ == '__main__':
    print("main init")
    main()

