# -*- coding: utf-8 -*-
# file created to share global variables troughout modules!
# will probably read and right to a config file!

#import ConfigController as cf

#todo: source selection
source = 0
defaultStart = 1#0 to menu, 1 to Local MP#, 2 To Bluetooth(have tom implement yet)
interval_r = 0
lastVolume = 80

if source == 0:
    #volume variables
    interval = 80
    min = 0
    max = 100
    step = 5
if source == 1:
#menu variables
    interval = 0
    min = 0
    max = 100
    step = 5

#left rotary config
l_clk    = 22
l_dt     = 27
l_btn    = 17

#right rotary config
r_clk    = 26
r_dt     = 6
r_btn    = 13



#status variable :todo, get the latest and save the current!
status = "pause"
second_status = ""

#music info, for now, only from bluetooth
music_info = []
next_music_info =  ""
#status messages in errors cases
message = ""


#initial musics folder
initFolder  = "/home/pi/Music/"
USBFolder   = ""
#local player variables
musicName   = ""
artist      = ""
album       = ""
time        = ""

#accepted audio files, so I avoid image and text files!
audioFormats =[
     ".3gp"
    ,".aa"
    ,".aac"
    ,".aax"
    ,".act"
    ,".aiff"
    ,".alac"
    ,".amr"
    ,".ape"
    ,".au"
    ,".awb"
    ,".dct"
    ,".dss"
    ,".dvf"
    ,".flac"
    ,".gsm"
    ,".iklax	"
    ,".ivs"
    ,".m4a"
    ,".m4b"
    ,".m4p"
    ,".mmf"
    ,".mp3"
    ,".mpc"
    ,".msv"
    ,".m3u"
    ,".ogg"
    ,".oga"
    ,".mogg"
    ,".opus"
    ,".ra"
    ,".rm"
    ,".raw"
    ,".rf64"
    ,".sln"
    ,".tta"
    ,".voc"
    ,".vox"
    ,".wav"
    ,".wma"
    ,".wv"
    ,".webm"
    ,".8svx"
    ,".cda"
    ,".flac"
]

#Basic Playback Status
random = True
repeatAll = False
repeatOne = True
totalSongs = 0

#fontawesome codes for icones https://fontawesome.com/v4.7.0/cheatsheet/
codes = ["\uf027"       #fa-volume-down - 51->80
         , "\uf6a9"     #mute -> 0%
         , "\uf026"     # fa-volume-off Low Audio 1 - > 50%
         , "\uf028"     #  fa-volume-up VolumeFull 80 -> 100%
         , "\uf28b"     # fa-pause-circle - pause
         , "\uf144"     # fa-play-circle - Play
         , "\uf049"     # fa-fast-backward previous   
         , "\uf050"     # fa-fast-forward next
         , "\uf074"     # fa-random - random     
         , "\uf021"     # fa-refresh - Repeat all
         , "\uf079" ]   # fa-retweet - repeat one

clicks = []