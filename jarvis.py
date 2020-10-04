import pyttsx3 # pip install pyttsx3
import datetime
import  speech_recognition as sr # pip install SpeechRecognition

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    speak("the current time is") 
    time()
    speak("the current date is") 
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternon sir") 
    elif hour >=18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")

    speak("jarvis at your service. please tell me how can i help you?")


def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizning...") 
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("say that again please...")

        return "None" 

    return query     

takeComand()



