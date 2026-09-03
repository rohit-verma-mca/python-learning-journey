<div align="center">

# 🐍 Python Learning Journey

**A structured, day-one log of learning Python — built while starting my MCA.**

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/python-learning-journey)

</div>

---

## About this repo

I'm an MCA student (BCA graduate) learning Python from the ground up. This repo is where
I track that process: concepts, my own notes, and solved practice questions — organized by
topic, not by whatever order I happened to watch/read things in.

It draws from two resources, merged into a single structured path instead of tracked
separately (since a lot of the early material overlaps):
- A **beginner-to-advanced video tutorial** covering Python fundamentals, OOP, and modules
- **"Automate the Boring Stuff with Python" (3rd Edition) by Al Sweigart** — practical automation

> I'm not claiming to have invented these exercises — the concepts and many practice
> questions come from the resources above. What's mine is the code, the notes, and the
> structure. Full attribution is in [Sources & Attribution](#sources--attribution).

## Table of Contents
- [Repository Structure](#repository-structure)
- [Progress](#progress)
- [Featured Projects](#featured-projects)
- [How to Run](#how-to-run)
- [Exercise Format](#exercise-format)
- [Sources & Attribution](#sources--attribution)

## Repository Structure

```
python-learning-journey/
├── 01-python-fundamentals/       Core language concepts
├── 02-automation-with-python/    Practical automation — the high-value material
├── 03-bonus-optional/            Extra topics, lower priority, come back later
├── 04-mini-projects/             Small builds combining multiple concepts
├── EXERCISE_FORMAT.md            The template every solved question follows
└── LICENSE
```

Every topic folder has its own `README.md` (concepts + my notes + a practice-question
tracker) and an `exercises/` folder with the solved code.

## Progress

### 01 — Python Fundamentals
- [ ] Python Basics & Variables
- [ ] Flow Control (if-else, conditionals)
- [ ] Loops
- [ ] Functions
- [ ] Debugging
- [ ] Lists & Tuples
- [ ] Dictionaries & Structuring Data
- [ ] Strings & Text Editing
- [ ] Numbers & Operators
- [ ] Classes & OOP
- [ ] Modules & Packages

### 02 — Automation with Python
- [ ] Regular Expressions
- [ ] Reading & Writing Files
- [ ] Organizing Files
- [ ] Command Line Programs
- [ ] Web Scraping
- [ ] Excel Spreadsheets
- [ ] PDF & Word Documents
- [ ] CSV, JSON & XML
- [ ] Scheduling & Launching Programs
- [ ] Email & Notifications

### 03 — Bonus / Optional
- [ ] Google Sheets
- [ ] SQLite Databases
- [ ] Graphs & Image Manipulation
- [ ] OCR (Recognizing Text in Images)
- [ ] GUI Automation (Keyboard & Mouse)
- [ ] Text-to-Speech & Speech Recognition

## Featured Projects
*(Fill this in as you complete real projects — this section is what visitors see first.)*

## Featured Projects

| Project | What it does | Folder |
|---|---|---|
| Automated File Organizer & Report Generator | Sorts files by type, generates an Excel report, and emails a summary — with logging and error handling | [`04-mini-projects/project_01`](04-mini-projects/project_01) |

## How to Run

```bash
git clone https://github.com/YOUR_USERNAME/python-learning-journey.git
cd python-learning-journey
python3 -m venv venv
source venv/bin/activate      # venv\Scripts\activate on Windows
pip install -r requirements.txt   # add this file once a project needs external packages
```

Each exercise file is self-contained — run it directly:
```bash
python 01-python-fundamentals/03_loops/exercises/q01_fizzbuzz.py
```

## Exercise Format

Every solved question follows one consistent template — see [`EXERCISE_FORMAT.md`](EXERCISE_FORMAT.md).
This matters more than it sounds: consistent, readable code across 50+ files is what makes
a repo look deliberate rather than dumped.

## Sources & Attribution

- Video tutorial — Python fundamentals, OOP, and beginner projects
- *Automate the Boring Stuff with Python*, 3rd Edition — Al Sweigart (free to read at
  [automatetheboringstuff.com](https://automatetheboringstuff.com), CC BY-NC-SA license)

All code in this repo is written/typed by me while working through these resources, for
learning purposes. Practice question prompts are paraphrased from the book/course where
applicable.

## How I Work

- One commit per real study session, with a message describing what was actually added
  (`Add regex practice: phone/email extractor` — not `update`)
- Notes are written in my own words, not copy-pasted
- No commits just to fill the contribution graph

---
<div align="center">
Started July 2026 &nbsp;·&nbsp; MCA Student &nbsp;·&nbsp; Learning in public
</div>
