
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pygame
import eel


import os
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

def start():
    eel.init("frontend") 
    play_assistant_sound()

    @eel.expose
    def init():
        eel.hideLoader()
        speak("Welcome to Jarvis")
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak("Welcome to Your Assistant")
            eel.hideStart()
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")
        
    os.system('start msedge.exe --app="http://127.0.0.1:5500/index.html"')

    try:
        eel.start("index.html", mode=None, host="localhost", port=5500, block=True)
    except KeyError as e:
        print(f"[EEL KeyError] Missing 'value' in message: {e}")
    except Exception as e:
        print(f"[EEL ERROR] {e}")

    print("Main file started...")

if __name__ == "__main__":
    print("Jarvis shuru ho raha hai...")
    start() 

