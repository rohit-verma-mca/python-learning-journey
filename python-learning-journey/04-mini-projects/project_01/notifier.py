"""
Project: Automated File Organizer & Report Generator
Day 4 — Email Notification (Part 1)

Sends an email notifying that the organizer has run, with a summary
of what was moved.
"""

import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.environ.get("EMAIL_APP_PASSWORD")

if not EMAIL_ADDRESS or not EMAIL_APP_PASSWORD:
    raise EnvironmentError(
        "EMAIL_ADDRESS and EMAIL_APP_PASSWORD must be set as environment variables before running this script."
    )


def send_summary_email(summary, recipient=None):
    if recipient is None:
        recipient = EMAIL_ADDRESS

    body_lines = ["Your file organizer just ran. Here's what happened:\n"]
    total = 0
    for category, count in summary.items():
        body_lines.append(f"  {category}: {count} file(s)")
        total += count
    body_lines.append(f"\nTotal files organized: {total}")

    msg = EmailMessage()
    msg["Subject"] = "File Organizer — Run Summary"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg.set_content("\n".join(body_lines))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        smtp.send_message(msg)

    print(f"Summary email sent to {recipient}")


if __name__ == "__main__":
    # standalone test with fake data
    test_summary = {"Documents": 3, "Images": 5, "Spreadsheets": 1, "Others": 2}
    send_summary_email(test_summary)