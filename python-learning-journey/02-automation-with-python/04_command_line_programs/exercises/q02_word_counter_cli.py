"""
Question:
Write a script that takes a filename as a command-line argument and
prints the number of lines, words, and characters in that file -
similar to the Unix "wc" command.

"""

import argparse


def count_file_stats(filename):
    with open(filename, "r") as f:
        content = f.read()

    lines = content.splitlines()
    words = content.split()

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": len(content),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines, words, and characters in a text file.")
    parser.add_argument("filename", help="Path to the text file")

    args = parser.parse_args()
    stats = count_file_stats(args.filename)

    print(f"Lines:      {stats['lines']}")
    print(f"Words:      {stats['words']}")
    print(f"Characters: {stats['characters']}")

# Run like this from the terminal:
# python q02_word_counter_cli.py some_file.txt