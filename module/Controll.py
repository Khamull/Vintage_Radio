#!/usr/bin/python3
from RPi import GPIO
import config as cf
from subprocess import DEVNULL, STDOUT, check_call
import AudioPlayer as ap
from time import sleep
from threading import Thread

class CONTROLL:
    def __init__(self):
        self.Mode           = cf.source
        self.l_clk          = cf.l_clk
        self.l_dt           = cf.l_dt
        self.l_btn          = cf.l_btn
        self.r_clk          = cf.r_clk
        self.r_dt           = cf.r_dt
        self.r_btn          = cf.r_btn
        self.isPaused       = False
        self.step           = cf.step
        self.preInterval    = self.interval = cf.interval
        self.min            = cf.min
        self.max            = cf.max
        self.isReseted      = False
        self.vlc_player     = None
        self.GPIO_setup()
        self.states_setup()
        self.set_volume()
       
    
    def GPIO_setup(self):
        #GPIO SETUP
        GPIO.setmode(GPIO.BCM)
        #left controll
        GPIO.setup(self.l_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.l_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.setup(self.l_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.setup(self.l_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        #right controll
        GPIO.setup(self.r_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.r_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.r_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def states_setup(self):
        self.l_clkLastState = GPIO.input(self.l_clk)
        #self.l_btnLastState = GPIO.input(self.l_btn)
        
        self.r_clkLastState = GPIO.input(self.r_clk)
        self.r_btnLastState = GPIO.input(self.r_btn)
        
 
    def add_event_callbakcs(self):
        
        print("GPIO event add called")
        #left control
        #GPIO.add_event_detect(self.l_btn,GPIO.RISING,callback=self.button_callback, bouncetime=300)
        
        GPIO.add_event_detect(self.l_clk,GPIO.FALLING,callback=self.interval_add_calc,bouncetime=20) 
        GPIO.add_event_detect(self.l_dt,GPIO.FALLING,callback=self.interval_remove_calc,bouncetime=20)
        
        #right controll
        GPIO.add_event_detect(self.r_clk,GPIO.FALLING,callback=self.next_callback,bouncetime=20)
        GPIO.add_event_detect(self.r_dt,GPIO.FALLING,callback=self.prev_callback,bouncetime=20)
        GPIO.add_event_detect(self.r_btn,GPIO.FALLING,callback=self.pause_button_callback,bouncetime=300)
        
    
    def interval_add_calc(self, channel):
        clkState = GPIO.input(self.l_clk)
        dtState = GPIO.input(self.l_dt)
        if clkState != self.l_clkLastState:
            if dtState != clkState:
                self.interval += self.step
                if self.interval > self.max:
                    self.interval = self.max
                cf.interval = self.interval
                self.set_volume()
                print(cf.interval)
            self.l_clkLastState = clkState
    
    def interval_remove_calc(self, channel):
        clkState = GPIO.input(self.l_clk)
        dtState = GPIO.input(self.l_dt)
        if dtState != self.l_clkLastState:
            if dtState != clkState:
                self.interval -= self.step
                if self.interval < self.min:
                    self.interval = self.min
                cf.interval = self.interval
                self.set_volume()
                print(cf.interval)
            self.l_clkLastState = clkState

        
    #volume controlled by left controll
    def set_volume(self):
        if cf.source == 0:
            #command = ["amixer", "cset", "numid=3", "{}%".format(cf.interval)]
            command = ["amixer", "cset", "numid=1", "{}%".format(cf.interval)]
            check_call(command, stdout=DEVNULL, stderr=STDOUT)
    
    def get_volume(self):
        command = ["amixer", "sget", "numid=1", "| awk -F'[][]' '{print $2}'"]
        self.interval = check_call(command, stdout=DEVNULL, stderr=STDOUT)
        #print(self.interval)
    #left controll
    def volume_state(self):
        volume = self.interval
        if self.isReseted:
            volume          = cf.lastVolume
            self.interval   = cf.lastVolume
            cf.interval     = cf.lastVolume
            self.isReseted = False
            #rint("Unmuted")
        else:
            cf.lastVolume = volume
            volume = 0
            self.isReseted = True
            cf.interval = volume
            self.interval = volume
            #print("Muted")
        self.set_volume() 
    
    #left button callback   
    def button_callback(self):
        print("Button CallBack")
        if cf.source == 0:
           #controls volume mute/unmute
           self.volume_state()
        if cf.source == 1:
            cf.interval = 0
            #gets the current selected menu option
            self.menu_control()
        if cf.source == 2:
            #gets the current selected menu option
           self.menu_control()
        if cf.source == 3:
            #gets the current selected menu option
           self.menu_control()
    
  
    #left menu controll   
    def menu_control(self):
        print("menu control")
        print(cf.source)
        
        if(cf.interval >= 0 and cf.interval <=25): 
            cf.source = 0
            self.isReseted = True
            #ap.play(self.vlc_player.player)
            #cf.interval = 50
            self.volume_state()
            #cf.defaultStart = 1
            print("Selected option 1")
        elif(cf.interval >= 26 and cf.interval <=50):
            cf.source = 2
            #cf.defaultStart = 2
            print("Selected option 2")
        elif(cf.interval >= 51 and cf.interval <=75):
            cf.source = 3
            print("Selected option 3")
        elif(cf.interval >= 76 and cf.interval <=100):
            cf.source = 4
            print("Selected option 4")
        
#        if cf.source == 0:
#            cf.interval = 80
#            self.set_volume_from_menu(80)
    #right button callback(probably to be better implemented)
    def pause_button_callback(self, channel):
        #btnPushed = GPIO.input(self.r_btn)
        if self.isPaused:
            self.isPaused = False
            print("Play")
            cf.status = "play"
            ap.play(self.vlc_player)
        else:
            self.isPaused = True
            print("Pause")
            cf.status = "pause"
            ap.pause(self.vlc_player)
        #self.r_btnLastState = btnPushed
    
    def next_callback(self, channel):
        clkState = GPIO.input(self.r_clk)
        dtState = GPIO.input(self.r_dt)
        if clkState != self.r_clkLastState:
            if dtState != clkState:
                ap.next(self.vlc_player)
                #print("Next")
        self.r_clkLastState = clkState
        self.player_status()

    def prev_callback(self, channel):
        clkState = GPIO.input(self.r_clk)
        dtState = GPIO.input(self.r_dt)
        if dtState != self.r_clkLastState:
            if dtState != clkState:
                ap.previous(self.vlc_player)
                #print("Previous")
        self.r_clkLastState = clkState
        self.player_status()
        
    def player_status (self):
        sleep(0.01)
        if ap.player_status(self.vlc_player):
            cf.status = "play"
        else:
            cf.status = "pause"
        cf.second_status = ""
    
    def get_music_info(self):
        try:
            cf.music_info = ap.music_info(self.vlc_player)
            #print(cf.music_info)
        except:
            pass
    
    def get_music_time(self):
        try:
            cf.time = ap.music_track_time(self.vlc_player)
            #print(cf.time)
        except:
            pass
            
    def get_palyer(self):
        self.vlc_player = ap.loadPlayer()
        
    def main(self):
        self.add_event_callbakcs()
        self.get_palyer()
        ap.play(self.vlc_player)

if __name__ == '__main__':
    print("main init")
    c = CONTROLL()
    c.main()
