"""
Question:
Write a program that simulates flipping a coin 100 times and counts how
many heads and tails occur. Then, in a copy of this working program,
introduce 2 small bugs on purpose, and fix them using what you learned
about reading tracebacks.
"""

import random


def flip_coins(num_flips=100):
    heads = 0
    tails = 0
    for _ in range(num_flips):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails


def solve():
    heads, tails = flip_coins(100)
    print(f"Heads: {heads}, Tails: {tails}")

    # --- Bug 1 (fixed) ---
    # Originally wrote: for _ in range(0, num_flips - 1)  -> off-by-one,
    # only flipped 99 times instead of 100. Fixed by using range(num_flips).

    # --- Bug 2 (fixed) ---
    # Originally wrote: if random.randint(0, 1) == "0"  -> compared an int
    # to a string, so it was always False and every flip counted as tails.
    # Fixed by comparing to the integer 0 instead of "0".


if __name__ == "__main__":
    solve()