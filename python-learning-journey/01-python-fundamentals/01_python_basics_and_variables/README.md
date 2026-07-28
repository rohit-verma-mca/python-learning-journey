## Python Basics & Variables

**Source:** Video tutorial + Book Ch.1 (Python Basics)

## Concepts covered
- Variables and how Python assigns values (no need to declare a type)
- Data types: `int`, `float`, `str`, `bool`
- Using `type()` to check a variable's data type
- Type conversion: `int()`, `float()`, `str()`
- `print()` and f-strings for output
- `input()` for taking user input (always returns a string)
- Naming conventions (snake_case, no starting with numbers, case-sensitive)

## My Notes
Python figures out a variable's type automatically based on the value you give it —
you never write the type yourself like in some other languages. A variable is really
just a name pointing to a value in memory. `input()` always gives back a string, even
if the user types a number, so you have to convert it yourself with `int()` or `float()`
before doing math with it.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Personal Profile Generator | ⬜ |
| 2 | Variable Swap Puzzle | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).