
import os
import webbrowser
import speech_recognition as sr
import win32com.client
import openai
from pyexpat import features

from sites import sitelist
from function_main import *
from gemini_test import *


# Global mode tracker
current_mode = "continue"  # "continue" = local, "internet" = AI mode

def set_mode(new_mode):
    global current_mode
    current_mode = new_mode

def get_mode():
    global current_mode
    return current_mode

# Setting the chatting features

def chat(query):
        pass

# todo:Add new mode funtionalities here

# This is for the internet mode using gemini api
def internetmode():
    say(f"You are in internet mode Say 'switch mode' to change.")
    while True:
        print("Listening (Internet mode)...")
        query = takecommand().lower()

        if "switch mode" in query:
            say("Switching back to Local Mode.")
            set_mode("continue")
            return  # Exit and let main loop handle switching

        resp = generate(query)   # Call Gemini
        if not os.path.exists("History_propmts"):
            os.mkdir("History_propmts")

        if resp:
            say(resp)
            print("AI:", resp)
            if ("write"or"draft"or"code" in query.lower()):
                prompt=(f"Jarvis said: "
                        f"________________________________________________________________________________________________"
                        f"{resp}"
                        f"________________________________________________________________________________________________"
                        f"You can now easily copy paste this as per your requirment :)")
                with open(f'History_propmts/{query[0:10]}.txt', 'w') as f:
                    f.write(resp)

# This is for the local mode of the AI
def localmode():
    sites = sitelist()
    say(f"You are in local mode Say 'switch mode' to change.")
    while True:
        print("Listening (Local mode)...")
        query = takecommand()

        # Check site commands
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f'Opening {site[0]}...')

        # Open Windsurf
        if 'open wind' in query.lower():
            windpath = r"C:\Users\shreyas\Downloads\Windsurf\Windsurf.exe"
            os.startfile(windpath)

        # Switch to internet mode
        if 'switch mode' in query.lower():
            say("Switching to Internet Mode.")
            set_mode("internet")
            return  # Exit and let main loop handle switching