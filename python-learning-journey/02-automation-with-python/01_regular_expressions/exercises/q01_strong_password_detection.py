"""
Question:
Write a function that uses regular expressions to make sure the password
string passed to it is strong. A strong password is defined as one that
is at least 8 characters long, contains both uppercase and lowercase
characters, and has at least one digit.

"""

import re


def solve(password):
    if len(password) < 8:
        return False
    if re.search(r"[A-Z]", password) is None:
        return False
    if re.search(r"[a-z]", password) is None:
        return False
    if re.search(r"\d", password) is None:
        return False
    return True


if __name__ == "__main__":
    test_cases = ["short1A", "longenough", "LongEnough1", "nouppercase1", "NoDigitsHere"]
    for pw in test_cases:
        print(f"{pw!r:20} -> {'Strong' if solve(pw) else 'Weak'}")