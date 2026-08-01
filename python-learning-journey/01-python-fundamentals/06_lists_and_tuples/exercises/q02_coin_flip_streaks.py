"""
Question:
Simulate flipping a coin 100 times per trial, across 10,000 trials, and
count how many trials contain a streak of at least 6 heads or 6 tails in
a row. Print what percentage of trials had such a streak.

Topic     : Lists, Loops
Source    : Automate the Boring Stuff with Python (3rd Ed.) - Ch.6 Practice Project ("Coin Flip Streaks")
Difficulty: Medium
"""

import random


def has_streak_of_six(flips):
    streak = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak += 1
            if streak >= 6:
                return True
        else:
            streak = 1
    return False


def run_trial(num_flips=100):
    return [random.choice(["H", "T"]) for _ in range(num_flips)]


def solve(num_trials=10000):
    trials_with_streak = 0

    for _ in range(num_trials):
        flips = run_trial()
        if has_streak_of_six(flips):
            trials_with_streak += 1

    percentage = (trials_with_streak / num_trials) * 100
    print(f"{trials_with_streak} out of {num_trials} trials had a streak of 6+ ({percentage:.2f}%)")
    return percentage


if __name__ == "__main__":
    solve()