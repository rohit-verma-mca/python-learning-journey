# Exercise / Question Format

Every solved question in this repo, in any folder, follows this template.
Consistency here is what makes a repo look deliberate to anyone browsing it.

**File naming:** `qXX_short_description.py`  (e.g. `q01_fizzbuzz.py`, `q02_comma_code.py`)

**Template:**

```python
"""
Question:
<Write the exact question / problem statement here>

Topic     : <e.g. Loops, Regular Expressions>
Source    : <e.g. Video tutorial - Loops section / Book Ch.9>
Difficulty: Easy / Medium / Hard
"""

def solve():
    pass


if __name__ == "__main__":
    solve()
```

**Rules:**
- One question per file.
- Docstring always has Question / Topic / Source / Difficulty.
- Wrap logic in a `solve()` function (or a clearly named equivalent) — not loose script code.
- Use `if __name__ == "__main__":` to demonstrate/test it.
- If a question has multiple valid approaches, add `solve_alternate()` in the same file
  instead of creating a second file.
- Keep comments meaningful — explain *why*, not just *what*.
