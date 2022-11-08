import pyttsx3 #text to speech 
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5') # sapi5 is speech application programming interface developed by microsoft 
voices=engine.getProperty('voices')
#print(voices[1].id) <- voice of zira
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('--email id --','--password--')
    server.sendmail('--email id--',to,content)
    server.close()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis sir Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir="--path--"
            songs=os.listdir(music_dir)
            print(songs)
            s=random.randint(0,2)
            os.startfile(os.path.join(music_dir,songs[s]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'email to me' in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="--email id--"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email")
        elif 'exit' in query:
            speak("okay have a good day sir")
            speak("bye")
            break
