"""
Question:
Write a function that takes a sentence and returns it with the words in
reverse order (e.g., "I love Python" -> "Python love I"), using .split()
and .join().

"""


def solve(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


if __name__ == "__main__":
    print(solve("I love Python"))          # Python love I
    print(solve("Automate the boring stuff"))  # stuff boring the Automate