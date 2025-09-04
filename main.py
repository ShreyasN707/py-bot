import os
import webbrowser
import speech_recognition as sr
import win32com.client
import openai
from sites import sitelist
from function_main import *
from gemini_test import *
from modes import *

# Global mode tracker
current_mode = "continue"  # "continue" = local, "internet" = AI mode



if __name__ == "__main__":
    print("Program started")
    say(f"Hey there!I am Blobber, A small guideline:"
        f"!local and internet are two modes!tell switch to change modes")

    # Main control loop
    while True:
        if get_mode() == "continue":
            localmode()
        elif get_mode() == "internet":
            internetmode()
