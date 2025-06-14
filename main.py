import speech_recognition as sr
import pyttsx3
import webbrowser

recognizor = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")


if __name__== "__main__":
    speak("jarvis activated sir how can i help you")
    
while True:
    r = sr.Recognizer()


    print("recognizing...")
    try:
        with sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source,timeout=2,phrase_time_limit=2)
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            speak("yes")

            with sr.Microphone() as source:
                print("jarvis active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)


    except Exception as e:
        print("Error; {0}".format(e))
