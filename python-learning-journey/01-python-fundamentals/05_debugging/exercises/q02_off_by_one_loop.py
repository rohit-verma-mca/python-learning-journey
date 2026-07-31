"""
Question:
Write a function that prints numbers 1 through 10 using range(). Include
an intentional off-by-one bug, explain what's wrong, then fix it.

"""


def print_numbers_buggy():
    # BUG: range(1, 10) only goes up to 9, missing 10 (off-by-one error)
    for i in range(1, 10):
        print(i)


def print_numbers_fixed():
    # FIX: range(1, 11) includes 10, since range() stops one before the end value
    for i in range(1, 11):
        print(i)


if __name__ == "__main__":
    print("Buggy version (misses 10):")
    print_numbers_buggy()
    print()
    print("Fixed version:")
    print_numbers_fixed()