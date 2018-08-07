#   python audio_threading.py
from pydub import AudioSegment
from pydub.playback import play
import pydub
import threading
import sys
import time


sound = (AudioSegment.from_file("No_Strings.mp4"))

def quit(x):
	while x:
		time.sleep(.1)

x= True
catch = threading.Thread(target=quit,args=[0])
catch.start()

music = threading.Thread(target=play,args=[sound],daemon=True)
music.start()

time.sleep(10)
x = False