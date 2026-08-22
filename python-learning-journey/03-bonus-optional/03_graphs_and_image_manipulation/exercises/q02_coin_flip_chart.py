"""
Question:
Run the Coin Flip Streaks simulation for a few different trial counts,
and plot the percentage of streaks found against trial count as a
simple line chart using matplotlib.

"""

import random
import matplotlib.pyplot as plt


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


def run_simulation(num_trials):
    trials_with_streak = 0
    for _ in range(num_trials):
        flips = run_trial()
        if has_streak_of_six(flips):
            trials_with_streak += 1
    return (trials_with_streak / num_trials) * 100


def solve():
    trial_counts = [100, 1000, 10000, 50000]
    percentages = []

    for count in trial_counts:
        percentage = run_simulation(count)
        percentages.append(percentage)
        print(f"{count} trials -> {percentage:.2f}% had a streak of 6+")

    plt.plot(trial_counts, percentages, marker="o")
    plt.xlabel("Number of Trials")
    plt.ylabel("Percentage with Streak of 6+")
    plt.title("Coin Flip Streaks: Percentage vs Trial Count")
    plt.xscale("log")
    plt.grid(True)
    plt.savefig("coin_flip_streaks_chart.png")
    print("\nChart saved as 'coin_flip_streaks_chart.png'")
    plt.show()


if __name__ == "__main__":
    solve()