"""
Project: Automated File Organizer & Report Generator
Day 2 — Excel Reporting

Takes the summary dictionary produced by organizer.py and generates a
clean Excel report of what was moved, with a timestamp.
"""

import openpyxl
from datetime import datetime


def generate_report(summary, output_folder="."):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Organizer Report"

    sheet.append(["Category", "Files Moved"])

    total_files = 0
    for category, count in summary.items():
        sheet.append([category, count])
        total_files += count

    sheet.append([])
    sheet.append(["Total", total_files])

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{output_folder}/organizer_report_{timestamp}.xlsx"
    wb.save(filename)

    print(f"\nReport saved: {filename}")
    return filename


if __name__ == "__main__":
    # quick standalone test with fake data
    test_summary = {"Documents": 3, "Images": 5, "Spreadsheets": 1, "Others": 2}
    generate_report(test_summary)