# Modules & Packages

**Source:** Video tutorial (pip, PyPI, random module, custom modules)

## Concepts covered
- Importing built-in modules (`import random`, `import math`, etc.)
- `from module import function` syntax
- Writing and importing your own custom modules
- `pip` and installing packages from PyPI
- `if __name__ == "__main__":` and why it matters when a file is imported vs run directly

## My Notes
A module is just a `.py` file — importing it runs that file's top-level code once and
gives you access to its functions/variables through the module name. `pip install`
downloads third-party packages from PyPI into your environment so you can import them
like built-in modules. Wrapping code in `if __name__ == "__main__":` means it only runs
when the file is executed directly, not when it's imported elsewhere — important once
you start splitting code across multiple files.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Table Printer as a Module | ⬜ |
| 2 | Custom Random Password Generator | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).