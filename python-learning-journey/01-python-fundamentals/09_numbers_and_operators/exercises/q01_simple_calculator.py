"""
Question:
Take two numbers and an operator (+, -, *, /) as input, and return the
result. Handle divide-by-zero with a try/except instead of letting it
crash.

"""


def solve(num1, operator, num2):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Error: cannot divide by zero"


if __name__ == "__main__":
    print(solve(10, "+", 5))   # 15
    print(solve(10, "-", 5))   # 5
    print(solve(10, "*", 5))   # 50
    print(solve(10, "/", 5))   # 2.0
    print(solve(10, "/", 0))   # Error: cannot divide by zero