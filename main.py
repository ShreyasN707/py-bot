from sites import sitelist
import webbrowser
import speech_recognition as sr
import win32com.client

# Initialize Windows TTS engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query= r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return say('some error')


if __name__ == "__main__":
    print("Program started")
    say("Hey there!!I am blobber")
    while True:
        print("Listening....")
        query = takecommand()

        sites=sitelist
        for site in sites:
            if f"open {site}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f'opening {site[1]}..')


        print(query)
