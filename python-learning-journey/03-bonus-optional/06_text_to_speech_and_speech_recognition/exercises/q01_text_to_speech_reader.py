"""
Question:
Write a script that takes a string of text and speaks it out loud using
pyttsx3.

Topic     : Text-to-Speech, pyttsx3
Source    : Automate the Boring Stuff with Python - Ch.24 (Text-to-Speech)
Difficulty: Easy
"""

import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("HI my name is Rohit , and i am pursuing MCA from kurukshetra university., nice to meet u all 😂")