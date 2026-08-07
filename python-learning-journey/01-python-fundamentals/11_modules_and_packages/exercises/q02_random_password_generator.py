"""
Question:
Using the built-in random module, write a function that generates a
random password of a given length, mixing letters, digits, and symbols.

"""

import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print(generate_password())        # default 12 characters
    print(generate_password(16))      # custom length
    print(generate_password(8))