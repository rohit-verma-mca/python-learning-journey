# Automated File Organizer & Report Generator

Scans a folder, automatically sorts files into subfolders by type (Documents, Images,
Spreadsheets, Others), generates an Excel report summarizing what was moved, and emails
a summary — all in one run.

## What it does
1. Scans a given folder for files sitting directly in it
2. Sorts each file into a subfolder based on its extension
3. Generates a timestamped Excel report of what was moved
4. Emails a summary of the run
5. Logs everything to both the terminal and a log file
6. Keeps working even if the email step fails (logs the failure instead of crashing)

## Tech used
- Python (`os`, `shutil`, `logging`, `argparse`, `smtplib`)
- `openpyxl` for the Excel report

## How to run

Install the one dependency:
```bash
pip install -r requirements.txt
```

Set your email credentials as environment variables (Gmail app password, not your real password):
```bash
$env:EMAIL_ADDRESS="youremail@gmail.com"
$env:EMAIL_APP_PASSWORD="your16digitapppassword"
```

Run it on the default test folder:
```bash
python organizer.py
```

Or point it at any folder:
```bash
python organizer.py "C:\Users\yourname\Downloads"
```

## What I learned building this
- Structuring a multi-file Python project instead of one script
- Replacing print statements with real logging (file + console output)
- Making scripts configurable via command-line arguments instead of hardcoded values
- Handling partial failure gracefully (one step failing shouldn't crash the whole pipeline)
- Keeping credentials out of code using environment variables