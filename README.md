<h1 id="welcome-to-my-vintage-radio-project-with-raspberry-pi">Welcome To My Vintage Radio Project With Raspberry Pi</h1>
<p>Hi! I’m building a custom head unit(not sure if I can call it that) for my vintage VW BUS, is a 1965 beauty(at least me and my wife think so).<br>
Here is a picture of part of it’s interior, as you can see, the space for the radio is very period specific, and, there are not much radios that can fit in there and does not need some type of adaptation, or cutting trough the metal.<br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/mediafiles/Wallpaper.jpg?raw=true" alt="enter image description here"></p>

<p>Looking at old vintage radios that are period accurate gave me an Ideia!<br>
<strong>"Why Not Use A RASPBERRY PI With Rotatry Encoder to replace the Radio?"</strong></p>
<p>And so, here we are.<br>
I’ve decided to use two rotary encoders to control the PI and a OLED Display to have some notion of what is going on. With, <strong>in the future</strong> some sensors like temperatur of the motor, it’s oil pressure, it’s tires pressure, stuff that might come in handy and we have in modern cars, but with a touch of the good old days!</p>
<p>I’m relatively new to Raspberry Pi and to Python, but, since I’m a programmer, what could go wrong, right?</p>
<p><strong>The Project so Far</strong><br>
I’ve managed to get the bearings of where I want to go, and decided I needed a model of my car’s panel, and, the Ideia looks like this:<br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/mediafiles/20200122_011818.jpg?raw=true" alt="enter image description here"><br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/mediafiles/20200122_011825.jpg?raw=true" alt="enter image description here"><br>

Still missing the OLED Display, I’m waiting for it to arrive.<br>
<strong>Update, just got the OLED Display, now another fun part begins!</strong><br>
Below Some Photos!<br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/mediafiles/20200303_161011.jpg?raw=true" alt="Front OLED Display"><br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/mediafiles/20200303_161328.jpg?raw=true" alt="Back Oled Display"><br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/mediafiles/20200303_161414.jpg?raw=true" alt="An Ideia of how it will look"><br>
Link to the one I bough, not the ideal one I was hopping, but will do :)<br>
<a href="https://pt.aliexpress.com/item/33024448944.html?spm=a2g0s.9042311.0.0.6b23b90aLRr6FO">https://pt.aliexpress.com/item/33024448944.html?spm=a2g0s.9042311.0.0.6b23b90aLRr6FO</a><br>
Had to tweak a little to get the disply working, and, since a few weeks have passed, here is a short video with the working test from LUMA Core, it worked like a charm once I figured out I had old connectors with issues in my jumpers:</p>
<p><a href="https://www.youtube.com/watch?v=o4S2uLBKm1A">https://www.youtube.com/watch?v=o4S2uLBKm1A</a></p>
<p><strong>I will list below the tutorial that get me going, the files that I’m using and what we have on them and will update the photos and progress accordingly :)</strong></p>
<h1 id="files">Files</h1>
<ul>
<li>Bluetooth_Media_Control
<ul>
<li>Basic Bluetooth Media realted functions, like Play and Pause, Music Name and Artist information</li>
</ul>
</li>
<li>Bluetooth_Pairing
<ul>
<li>Anything Related to the process of configuring the PI as a Bluetooth Audio Receiver</li>
</ul>
</li>
<li>DevTests
<ul>
<li>Tests, loads of them, since I’m unfamiliar with Python and I do like trial and error</li>
</ul>
</li>
<li>Misc
<ul>
<li>So far, the MISC section is just a basic shutdown that will be converted in a service, and will be waiting for a signal, right now, it is waiting for a 10s button push.</li>
</ul>
</li>
<li>Volume_Control
<ul>
<li>I’ve started here, trying to figure out how to control the volume with ALSA Mixer and the Rotary Encoder.</li>
</ul>
</li>
<li>module
<ul>
<li>I've advanced in python studys and had the clever ideia of keeping the working solution in a specific folder, the code that is working, is in module folder!
</ul>
</li>
<li><a href="http://ReadME.md">ReadME.md</a> - this File</li>
</ul>
<h1 id="tutorials-and-useful-links">Tutorials and Useful Links</h1>
<p>One of the first things I found out is that the onboard bluetooth adapter from the PI has some issues when working with Wifi, and, at least during development, I will be using Wifi, so, I bought a Bluetooth Dongle and disabled the onboard adapter following the instructions on this link:<br>
<a href="https://www.raspberrypi.org/forums/viewtopic.php?t=178485">https://www.raspberrypi.org/forums/viewtopic.php?t=178485</a></p>
<p>After that, I do have to confirgure the Bluetooth to be a audio Sync, and this two tutorials helped me a lot to understand what I was supossed to do.</p>
<p><a href="https://docs.google.com/document/d/12cK4heNd7kY3jYZI_sW1AD407dn_ds-9zZdX4qs-TJg/edit#">https://docs.google.com/document/d/12cK4heNd7kY3jYZI_sW1AD407dn_ds-9zZdX4qs-TJg/edit#</a><br>
<a href="https://gist.github.com/oleq/24e09112b07464acbda1">https://gist.github.com/oleq/24e09112b07464acbda1</a></p>
<p>Small e-book with a series of basic “how to” tutorials!<br>
<a href="https://books.google.com.br/books?id=xYhMlilTwC4C&amp;pg=PA105&amp;lpg=PA105&amp;dq=counting+the+times+a+button+is+pushed+in+python+raspberry+pi&amp;source=bl&amp;ots=W4bdeBlepX&amp;sig=ACfU3U0q5Chr5-g-Src6fnVqU8M5HSBflQ&amp;hl=pt-BR&amp;sa=X&amp;ved=2ahUKEwim1dLHrKTnAhUFK7kGHWNmANoQ6AEwAnoECAoQAQ#v=onepage&amp;q=counting%20the%20times%20a%20button%20is%20pushed%20in%20python%20raspberry%20pi&amp;f=false">https://books.google.com.br/books?id=xYhMlilTwC4C&amp;pg=PA105&amp;lpg=PA105&amp;dq=counting+the+times+a+button+is+pushed+in+python+raspberry+pi&amp;source=bl&amp;ots=W4bdeBlepX&amp;sig=ACfU3U0q5Chr5-g-Src6fnVqU8M5HSBflQ&amp;hl=pt-BR&amp;sa=X&amp;ved=2ahUKEwim1dLHrKTnAhUFK7kGHWNmANoQ6AEwAnoECAoQAQ#v=onepage&amp;q=counting the times a button is pushed in python raspberry pi&amp;f=false</a></p>
<p>This Tutorial/Solution helped me to avoid false hits specially in the RightControl(next/prev/pause/play functions)<br>
<a href="https://www.raspberrypi.org/forums/viewtopic.php?t=134394">https://www.raspberrypi.org/forums/viewtopic.php?t=134394</a></p>
<p>Bluetooth Audio controll using bus<br>
<a href="https://scribles.net/controlling-bluetooth-audio-on-raspberry-pi/">https://scribles.net/controlling-bluetooth-audio-on-raspberry-pi/</a><br>
They will be listed here, and probably separeted by function that I used them.</p>
<p>[Edit] Using Luma was the best choice all along, their step by step for hardware and software for SSD1309 worked like a charm!</p>
<p>Since I do not have any of the adafruit easy to use displays, and my is a SSD1309, I’m going to follow the answer from this guy and test Luma<br>
<a href="https://raspberrypi.stackexchange.com/questions/106288/how-to-connect-raspberry-pi-4-to-sparkfun-ssd1306-ssd1309-oled-transparent-dis">https://raspberrypi.stackexchange.com/questions/106288/how-to-connect-raspberry-pi-4-to-sparkfun-ssd1306-ssd1309-oled-transparent-dis</a><br>
<a href="https://luma-oled.readthedocs.io/en/latest/python-usage.html">https://luma-oled.readthedocs.io/en/latest/python-usage.html</a><br>
Starting by getting PIP or Pillow, not sure what does what right now!<br>
<a href="https://pillow.readthedocs.io/en/latest/installation.html">https://pillow.readthedocs.io/en/latest/installation.html</a></p>
Started Using VLC Python, was a bit dificult to understand it's documentantion, but here it is the links I used:
https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Meta-class.html
Specially, the ones that gives us the basic usage of the methods, that are, IMO poorly organized, but man, do they have functions to media and network capabilities! 

https://github.com/OSUrobotics/vlc/blob/master/src/vlc/libvlc.py
https://www.programcreek.com/python/example/93375/vlc.Instance

Was working on my own random function to load the playlists, and here is a simpler solution
https://pynative.com/python-random-shuffle/

Steps to make Luma Core to Work

1 - Pip Install
https://pillow.readthedocs.io/en/latest/installation.html
2 - Luma.Core
https://luma-oled.readthedocs.io/en/latest/install.html
3 - Install Python VLC


<!--stackedit_data:
eyJkaXNjdXNzaW9ucyI6eyIwZzVaVHp5ck9WT204c0ZVIjp7In
RleHQiOiJlbnRlciBpbWFnZSBkZXNjcmlwdGlvbiBoZXJlIiwi
c3RhcnQiOjUxMCwiZW5kIjo1MTB9fSwiY29tbWVudHMiOnsiYT
daMkpnOFJkWTdVSTdpRiI6eyJkaXNjdXNzaW9uSWQiOiIwZzVa
VHp5ck9WT204c0ZVIiwic3ViIjoiZ2g6NTc3ODQwNCIsInRleH
QiOiJEYXNoIFZpZXcgb24gYSBDb2xkIERheSBXaXRoIGEgRGlu
byIsImNyZWF0ZWQiOjE1OTIzMzIwNDYyNTF9fSwiaGlzdG9yeS
I6WzE5MjEzNzc5MzUsMTgyNDIyOTM3Nyw2MjA3MzE2NzddfQ==

-->
