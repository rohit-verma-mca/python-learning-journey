# Lists & Tuples

**Source:** Video tutorial + Book Ch.6 (Lists)

## Concepts covered
- Creating and indexing lists
- Slicing (`list[start:end]`)
- List methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`
- Tuples vs lists (mutable vs immutable)
- Tuple unpacking
- The `in` and `not in` operators
- Looping over lists with `for` and `enumerate()`

## My Notes
Lists can be changed after creation (mutable) — you can add, remove, or reorder items.
Tuples look similar but can't be changed once made (immutable), which makes them useful
for data that shouldn't accidentally get modified, like coordinates. Tuple unpacking
lets you assign multiple variables from one tuple in a single line, like `x, y = point`.

## Notable Practice Projects (from the book)
- **Comma Code** — join a list into a readable sentence with commas and 'and'
- **Coin Flip Streaks** — simulate 10,000 trials to find how often a streak of 6 heads/tails occurs

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Comma Code | ✅ |
| 2 | Coin Flip Streaks | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).