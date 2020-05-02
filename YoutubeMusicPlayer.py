import os
import requests
import urllib.request
import urllib.parse
import re
import sys
import time
import webbrowser as wb
from gtts import gTTS
def speech_audio(mytext):
    myobj = gTTS(mytext)
    myobj.save("welcome1.mp3")
    os.system("welcome1.mp3")

print('justrohit\t MUSIC PLAYER!')
print('\n---------------------------------\n')
#audio file

time.sleep(3)
while True:
    song_name = (input("Name of the track: "))
    query_string = urllib.parse.urlencode({"search_query" : song_name})
    print('\n')

    speech_audio('There you go! Play it.')
    time.sleep(3)

    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    text_format=("http://www.youtube.com/watch?v=" + search_results[0])

    wb.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
    print('Sorry for the advertisements')
    time.sleep(15)

    print('Do you want to run another? \n')
    print()
    choice=input()
    print('\n')

    if choice== 'Y' or 'y' or 'yes' or 'Yes' or "YES":
        pass
    else:
        break
