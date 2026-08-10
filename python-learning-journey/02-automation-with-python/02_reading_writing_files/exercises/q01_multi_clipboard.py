"""
Question:
Write a program that lets you save named text snippets to a file
(store them as JSON), then retrieve and print one by name when you
pass its keyword.

Topic     : File I/O, JSON
Source    : Automate the Boring Stuff with Python - Ch.10 Practice Project ("Extending the Multi-Clipboard")
Difficulty: Medium
"""

import json
import os

DATA_FILE = "clipboard_data.json"


def load_clipboard():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_snippet(keyword, text):
    data = load_clipboard()
    data[keyword] = text
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_snippet(keyword):
    data = load_clipboard()
    return data.get(keyword, "No snippet found for that keyword.")


if __name__ == "__main__":
    save_snippet("agree", "I agree. That sounds fine to me.")
    save_snippet("busy", "I'm currently busy, I'll get back to you soon.")

    print(get_snippet("agree"))
    print(get_snippet("busy"))
    print(get_snippet("missing"))