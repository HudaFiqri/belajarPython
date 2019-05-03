import pyttsx3
import speech_recognition as sr
import os
import wolframalpha

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[len(voices)-1].id)

def speak(audio):
    print('computer = '+audio)
    engine.say(audio)
    engine.runAndWait()

speak('halo master')

