def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


def solve():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    while number != 1:
        number = collatz(number)


if __name__ == "__main__":
    solve()