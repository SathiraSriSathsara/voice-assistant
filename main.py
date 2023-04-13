import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def get_text():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello! How can I help you?")

while True:
    text = get_text()

    if "hello" in text:
        speak("Hello! How can I help you?")

    elif "what's your name" in text:
        speak("My name is ChatGPT, I'm a virtual assistant created by OpenAI.")

    elif "how are you" in text:
        speak("I'm doing well, thank you for asking.")

    elif "what time is it" in text:
        import datetime
        now = datetime.datetime.now()
        speak("It's " + now.strftime("%H:%M"))

    elif "goodbye" in text:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I didn't understand what you said.")
