import pandas as pd
import numpy as np
import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import wikipedia
import os
import timeit

def speechToText():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            start = timeit.default_timer()
            return(r.recognize_google(audio))
            stop = timeit.default_timer()
            timeTaken = stop - start
            print("Time taken: "+ str(timeTaken))
        except Exception as e:
            print("Error: "+str(e))
        return "Error"
       
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

while True:
          
    query = speechToText().lower()
          
        
    if 'wikipedia' in query:
        print("You: "+query)
        speak('Searching Wikipedia...')
        print('Jarvis: Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print("Jarvis: According to Wikipedia")
        print(results)
        speak(results)
            
    elif 'search' in query:
        speak('Making a Google Search..')
        query = query.replace("search", "")
        query = list(query.split())
        speak('Searching..')
        url="https://www.google.com/search?q="
        for word in query:
            url = url + word + "+"
            url = url[:-1]
            webbrowser.open(url)
            
    elif 'open youtube' in query:
        print("You: "+query)
        speak("Here you go to Youtube\n")
        print("Jarvis: Here you go to Youtube\n")
        webbrowser.open("youtube.com")
  
    elif 'open google' in query:
        print("You: "+query)
        speak("Here you go to Google\n")
        print("Jarvis: Here you go to Google\n")
        webbrowser.open("google.com")
  
    elif 'open stack overflow' in query:
        print("You: "+query)
        speak("Here you go to Stack Over flow.Happy coding")
        print("Jarvis: Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
        
    elif 'who are you' in query:
        print("You: "+query)
        speak("Hello, Sir! I am Jarvis your personal assistant. How can I help you?")
        print("Jarvis: Hello, Sir! I am Jarvis your personal assistant. How can I help you?")

    elif 'how are you' in query:
        print("You: "+query)
        speak("I am fine, Thank you")
        print("Jarvis: I am fine, Thank you")
        speak("How are you, Sir")
        print("Jarvis: How are you, Sir")

    elif 'fine' in query or "good" in query:
        print("You: "+query)
        speak("It's good to know that your fine")
        print("Jarvis: It's good to know that your fine")

    elif "who made you" in query or "who created you" in query:
        print("You: "+query)
        speak("I have been created by Sir Harsh.")
        print("I have been created by Sir Harsh.")

    elif 'joke' in query:
        print("You: "+query)
        speak(pyjokes.get_joke())

    elif "who am i" in query:
        print("You: "+query)
        speak("If you talk then definately your human.")
        print("Jarvis: If you talk then definately your human.")

    elif "why you came to world" in query:
        print("You: "+query)
        speak("Thanks to Harsh. Further It's a secret")
        print("Jarvis: Thanks to Harsh. Further It's a secret")

    elif 'exit' or 'bye' in query:
        print("You: "+query)
        speak("Thanks for giving me your time. It was really nice talking to you!")
        print("Jarvis: Thanks for giving me your time. It was really nice talking to you!")
        break;
        
    else:
        print("You: "+query)
        speak("I did not get you ! Could you please say it again")
        print("Jarvis: I did not get you ! Could you please say it again!")