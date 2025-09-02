import os
from sites import sitelist
import webbrowser
import speech_recognition as sr
import win32com.client
import openai

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query= r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            say('Sorryy couldn\'t catch it ')
            return ' '


# Initialize Windows TTS engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
    speaker.Speak(text)