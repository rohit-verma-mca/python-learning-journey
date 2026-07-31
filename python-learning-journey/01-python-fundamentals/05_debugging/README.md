# Debugging

**Source:** Book Ch.5 (Debugging) — reading tracebacks, assertions, logging vs print

## Concepts covered
- Reading Python tracebacks (reading them bottom-up, not top-down)
- Common error types: `SyntaxError`, `NameError`, `TypeError`, `IndexError`, `KeyError`
- `assert` statements for catching bugs early
- The `logging` module vs using `print()` for debugging
- Using a debugger / breakpoints in VS Code

## My Notes
The most useful line in a traceback is usually the last one — it tells you the actual
error type and message, while the lines above show the chain of calls that led there.
`assert` statements crash the program immediately with a clear message if a condition
you expect to be true turns out false — useful for catching bugs before they cause
confusing behavior later. `logging` is better than scattering `print()` statements
everywhere because you can leave it in the code and turn it on/off by severity level.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Debugging Coin Toss | ⬜ |
| 2 | Find and Fix: Off-by-One Loop | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).