from importlib import import_module


import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")

    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("This is jarvis! How may i help you?")

def takeCommand():

    # it takes microphone input from the user and returns string output!

   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print("e")
        print("Say that again please..")
        return "None" 
    return query
if __name__ == "__main__":
    wishme() 

    while True:
    
        query = takeCommand().lower()

# Logic for executing tasks based on

        

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'Mountains' in query:
            speak("you can visit Kashmir to spend time in mountains")

        elif 'animal' in query:
            speak("Dogs are my favourite animal because they serve loyalty")

      