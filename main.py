import os
from sites import sitelist
import webbrowser
import speech_recognition as sr
import win32com.client
import openai
from function_main import *



if __name__ == "__main__":
    print("Program started")
    say("Hey there!!I am blobber")

    sites = sitelist()
    while True:
        print("Listening....")
        query = takecommand()

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f'opening {site[0]}...')
        print(query)

        if 'open image' in query:
            musicpath=r"C:\Users\shreyas\OneDrive\Pictures\Screenshots"
            os.startfile(musicpath)
