# GUI Automation — Keyboard & Mouse

**Source:** Book Ch.23

## Concepts covered
- The `pyautogui` module
- Controlling the mouse: `.moveTo()`, `.click()`, `.dragTo()`
- Controlling the keyboard: `.write()`, `.press()`, `.hotkey()`
- Taking screenshots and locating images on screen with `.locateOnScreen()`
- The "fail-safe" feature (moving mouse to a corner to abort a runaway script)

## My Notes
`pyautogui` controls the actual mouse and keyboard on the computer, the same way a human
would — it doesn't know about "web pages" or "apps," it just moves the cursor to pixel
coordinates and sends keystrokes, so it works on literally anything visible on screen.
This makes it powerful but also risky — a bug can click or type in the wrong place
completely silently. The built-in fail-safe (yanking the mouse to a screen corner)
exists specifically because early testers kept accidentally locking up their own
computers with runaway scripts.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Auto-Typer with Countdown | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).