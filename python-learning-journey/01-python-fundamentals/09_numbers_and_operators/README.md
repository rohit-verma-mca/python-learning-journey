# Numbers & Operators

**Source:** Video tutorial

## Concepts covered
- Arithmetic operators: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent)
- Operator precedence (PEMDAS)
- `int` vs `float` and automatic type promotion
- Augmented assignment operators: `+=`, `-=`, `*=`, `/=`
- `round()` and formatting numbers for display

## My Notes
`/` always gives a float result in Python 3, even if both numbers divide evenly —
`//` is what gives you a whole-number (floor) result. `%` gives the remainder of a
division, which is useful for checking things like even/odd or wrapping values around
a range. Python follows standard math operator precedence, so `**` runs before
`*`/`/`, which run before `+`/`-`.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Simple Calculator | ⬜ |
| 2 | Compound Interest Calculator | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).