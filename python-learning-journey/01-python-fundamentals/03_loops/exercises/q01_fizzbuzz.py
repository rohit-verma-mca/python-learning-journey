"""
Question:
Write a program that prints numbers from 1 to 100.
But for multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz".
For multiples of both 3 and 5, print "FizzBuzz".

Topic     : Loops, Conditionals
Source    : Video tutorial - Loops section (classic FizzBuzz exercise)
Difficulty: Easy
"""


def solve(n=100):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    solve()
