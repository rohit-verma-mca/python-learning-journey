"""
Question:
Write a script that gives a 5-second countdown (so you can click into a
safe text box), then automatically types out a short sentence using
pyautogui.write().

"""

import time
import pyautogui

pyautogui.FAILSAFE = True  # move mouse to any screen corner to abort instantly


def countdown(seconds=5):
    print("Click into Notepad (or any text box) now!")
    for i in range(seconds, 0, -1):
        print(f"Typing starts in {i}...")
        time.sleep(1)


def auto_type(text):
    pyautogui.write(text, interval=0.05)


if __name__ == "__main__":
    countdown(5)
    auto_type("Hello, this text was typed automatically by pyautogui!")
    print("Done typing.")