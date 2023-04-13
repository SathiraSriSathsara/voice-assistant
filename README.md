# Python Voice Assistant

In the code I provided, we created a virtual assistant using Python. A virtual assistant is like a computer program that can understand what you say and respond to your questions or commands. It's like having a robot friend that you can talk to!

To make the virtual assistant work, we used a few libraries in Python. A library is like a set of tools that we can use to help us write our code. The libraries we used in this code help us to recognize what you say and say something back to you.

The first thing the virtual assistant does is ask you to say something. You can say anything you want, and the virtual assistant will try to understand what you're saying. It does this using a process called speech recognition. Speech recognition is like magic! It listens to the sounds you make when you talk and turns them into words that the computer can understand.

Once the virtual assistant understands what you said, it will try to respond to you. It does this using a process called text-to-speech. Text-to-speech is also like magic! It turns the words the computer wants to say into sounds that you can hear.

In the code, we wrote a few phrases that the virtual assistant knows how to respond to. For example, if you say "hello", the virtual assistant will say "Hello! How can I help you?". If you say "what's your name", it will say "My name is ChatGPT, I'm a virtual assistant created by OpenAI". If you say "goodbye", it will say "Goodbye!" and stop working.

That's a basic explanation of how the virtual assistant works!

## Installation (Libraries)

First, you need to install the following libraries using pip and you can install these libraries by running the following commands on your command prompt or terminal:
   
📌 SpeechRecognition

```bash
pip install SpeechRecognition
```

📌 pyttsx3

```bash
pip install pyttsx3
```

📌 PyAudio

```bash
pip install PyAudio
```

## Make your own - Step by Step
Once you have installed the libraries, create a Python script and import the necessary libraries: 

```python
import speech_recognition as sr
import pyttsx3
```
Then, create an instance of the Recognizer class from the speech_recognition library:

```bash
r = sr.Recognizer()
```
Next, use the pyttsx3 library to create an instance of the Engine class and set the voice:
```bash
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # set the voice to the first one in the list
```
Now, define a function to take voice input and return the recognized text using the Recognizer instance:
```bash
def get_text():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""
```
Finally, define a function to use the pyttsx3 library to speak the given text:
```bash
def speak(text):
    engine.say(text)
    engine.runAndWait()
```
Now, you can use these functions to create a basic virtual assistant. Here's an example:
```bash
while True:
    text = get_text().lower()

    if "hello" in text:
        speak("Hello! How can I help you?")

    elif "what's your name" in text:
        speak("My name is ChatGPT, I'm a virtual assistant created by OpenAI.")

    elif "goodbye" in text:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I didn't understand what you said.")
```
This code will listen to your voice input and respond to specific phrases. You can add more phrases and functionality to create a more sophisticated virtual assistant.




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


