"""
Question:
Say you have a list value like this:
    spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a
string with all the items separated by a comma and a space, with "and"
inserted before the last item. For example, passing the spam list to
the function should return:
    'apples, bananas, tofu, and cats'
The function should work with any list passed to it, including an
empty list.

Topic     : Lists, Strings
Source    : Automate the Boring Stuff with Python (3rd Ed.) - Ch.6 Practice Project ("Comma Code")
Difficulty: Easy
"""


def solve(items):
    if len(items) == 0:
        return ""
    if len(items) == 1:
        return items[0]

    result = ", ".join(items[:-1])
    result += ", and " + items[-1]
    return result


if __name__ == "__main__":
    spam = ["apples", "bananas", "tofu", "cats"]
    print(solve(spam))
    # Output: apples, bananas, tofu, and cats

    print(solve([]))       # Output: (empty string)
    print(solve(["cat"]))  # Output: cat
