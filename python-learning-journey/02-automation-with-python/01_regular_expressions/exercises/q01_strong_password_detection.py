"""
Question:
Write a function that uses regular expressions to make sure the password
string passed to it is strong. A strong password is defined as one that
is at least 8 characters long, contains both uppercase and lowercase
characters, and has at least one digit.
(Hint: it's easier to test the string against several regex patterns
than to write one single regex that checks every rule at once.)

Topic     : Regular Expressions
Source    : Automate the Boring Stuff with Python (3rd Ed.) - Ch.9 Practice Program ("Strong Password Detection")
Difficulty: Medium
"""

import re


def solve(password):
    if len(password) < 8:
        return False
    if re.search(r"[A-Z]", password) is None:      # needs an uppercase letter
        return False
    if re.search(r"[a-z]", password) is None:      # needs a lowercase letter
        return False
    if re.search(r"\d", password) is None:          # needs at least one digit
        return False
    return True


if __name__ == "__main__":
    test_cases = ["short1A", "longenough", "LongEnough1", "nouppercase1", "NoDigitsHere"]
    for pw in test_cases:
        print(f"{pw!r:20} -> {'Strong' if solve(pw) else 'Weak'}")
