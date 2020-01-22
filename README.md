---


---

<h1 id="welcome-to-my-vintage-radio-project-with-raspberry-pi">Welcome To My Vintage Radio Project With Raspberry Pi</h1>
<p>Hi! I’m building a custom head unit(not sure if I can call it that) for my vintage VW BUS, is a 1965 beuaty(at least me and my wife think so.<br>
Here is a picture of part of it’s interior, as you can see, the space for the radio is very time specific, and, there are not much radios that can fit in there and does not need some type of adaptation, or cutting trough the metal.<br>
<img src="https://scontent.fcgh11-1.fna.fbcdn.net/v/t1.0-9/43462799_309476856304772_5431551599711354880_o.jpg?_nc_cat=101&amp;_nc_oc=AQmifq89rNEnwnpwOIC42puo4Ow970gbRcCEg4C2xV-H1epM3RZIuB6Ywca6f8DWKjI&amp;_nc_ht=scontent.fcgh11-1.fna&amp;oh=068ccf13b89e9b637ea71835ffe35e19&amp;oe=5ED81DF3" alt="enter image description here"></p>
<p>Looking at old vintage radios that are period accurate gave an Ideia!<br>
<strong>"Why Not Use A RASPBERRY PI With Rotatry Encoder to replace the Radio?"</strong></p>
<p>And so, here we are.<br>
I’ve decided to use two rotary encoders to control the PI and a OLED Display to have some notion of what is going on. With, <strong>in the future</strong> some sensors like temperatur of the motor, it’s oil pressure, it’s tires pressure, stuff that might come in handy and we have in modern cars, but with a touch of the good old days!</p>
<p>I’m relatively new to Raspberry Pi and to Python, but, since I’m a programmer, what could go wrong, right?</p>
<p><strong>The Project so Far</strong><br>
I’ve managed to get the bearings of where I want to go, and decided I needed a model of my car’s panel, and, the Ideia looks like this:<br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/20200122_011818.jpg?raw=true" alt="enter image description here"><br>
<img src="https://github.com/Khamull/Vintage_Radio/blob/master/20200122_011825.jpg?raw=true" alt="enter image description here"><br>
<strong>Still missing the OLED Display, I’m waiting for it to arrive.</strong></p>
<p>I will list below the tutorial that get me going, the files that I’m using and what we have on them and will update the photos and progress accordingly :)</p>
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
<li><a href="http://ReadME.md">ReadME.md</a> - this File</li>
</ul>
<h1 id="tutorials-and-useful-links">Tutorials and Useful Links</h1>
<p>They will be listed here, and probably separeted by function that I used them.</p>

