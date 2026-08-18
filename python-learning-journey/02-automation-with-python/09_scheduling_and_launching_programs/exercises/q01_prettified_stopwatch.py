"""
Question:
Write a stopwatch program - pressing Enter starts it, pressing Enter
again records a "lap" and prints the lap time and total elapsed time,
formatted cleanly (not just raw seconds).

"""

import time


def format_time(seconds):
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes:02d}:{secs:05.2f}"


def solve():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    last_lap_time = start_time
    lap_number = 1

    print("Stopwatch started! Press Enter to record a lap, or type 'stop' to end.")

    while True:
        user_input = input()
        if user_input.strip().lower() == "stop":
            break

        now = time.time()
        lap_duration = now - last_lap_time
        total_duration = now - start_time

        print(f"Lap {lap_number}: {format_time(lap_duration)}  |  Total: {format_time(total_duration)}")

        last_lap_time = now
        lap_number += 1

    print("Stopwatch stopped.")


if __name__ == "__main__":
    solve()