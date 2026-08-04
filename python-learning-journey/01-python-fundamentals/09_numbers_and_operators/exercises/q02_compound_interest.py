"""
Question:
Take a principal amount, annual interest rate, and number of years as
input, and calculate the final amount using the compound interest
formula A = P * (1 + r/100) ** t. Print the result rounded to 2
decimal places.

"""


def solve(principal, rate, years):
    amount = principal * (1 + rate / 100) ** years
    return round(amount, 2)


if __name__ == "__main__":
    result = solve(10000, 8, 5)
    print(f"Final amount: {result}")   # Final amount: 14693.28

    result2 = solve(5000, 6.5, 3)
    print(f"Final amount: {result2}")