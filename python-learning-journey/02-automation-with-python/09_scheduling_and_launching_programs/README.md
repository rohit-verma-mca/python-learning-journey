# Keeping Time, Scheduling Tasks & Launching Programs

**Source:** Book Ch.19

## Concepts covered
- The `time` and `datetime` modules
- `time.sleep()` for delays
- Formatting dates/times with `strftime()`
- The `schedule` module for running tasks on a recurring basis
- Launching other programs/scripts with `subprocess`

## My Notes
`time.sleep(seconds)` pauses execution for that many seconds — useful for polling
loops or spacing out repeated actions. `datetime.now()` gives the current date/time as
an object you can format however you want with `strftime()`. The `schedule` module lets
you say "run this function every day at 9am" in plain code, but it only works while the
script keeps running (usually inside a `while True` loop) — it doesn't run in the
background on its own once the script exits.

## Notable Practice Projects (from the book)
- **Prettified Stopwatch** — track lap times with clean formatted output
- **Scheduled Web Comic Downloader** — combine web scraping with scheduling to run automatically

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Prettified Stopwatch | ⬜ |
| 2 | Scheduled Web Comic Downloader | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).