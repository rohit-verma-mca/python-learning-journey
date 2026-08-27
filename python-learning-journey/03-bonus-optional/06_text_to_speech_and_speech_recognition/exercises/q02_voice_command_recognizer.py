"""
Question:
Write a script that listens through the microphone for a few seconds
and prints back what it heard as text, using speech_recognition.

"""

import speech_recognition as sr


def listen_and_transcribe():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening now... speak something!")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    print("Processing...")
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not reach the speech recognition service: {e}")


if __name__ == "__main__":
    listen_and_transcribe()