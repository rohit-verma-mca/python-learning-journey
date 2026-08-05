# Classes & OOP

**Source:** Video tutorial (constructors, inheritance)

## Concepts covered
- Defining a class with `class`
- The `__init__` constructor and `self`
- Instance attributes vs methods
- Inheritance — subclasses extending a base class
- Overriding methods in a subclass
- `__str__` for readable printed output

## My Notes
A class is a blueprint for creating objects — `__init__` runs automatically whenever
you create a new instance, setting up its starting attributes. `self` refers to the
specific instance the method is being called on, which is why it's the first parameter
in every method. Inheritance lets a subclass reuse a parent class's code and only
override the parts that need to be different, instead of rewriting everything.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Emoji Translator Class | ⬜ |
| 2 | Vehicle Class with Inheritance | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).