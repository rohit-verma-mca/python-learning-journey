"""
Question:
Given a list of people and a list of chores, randomly assign one chore
to each person and email each person their assigned chore.

"""

import os
import random
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.environ.get("EMAIL_APP_PASSWORD")

# Using dummy emails here for testing - swap in real ones only if you want to actually send
people = {
    "Rahul": "rahul_test@example.com",
    "Priya": "priya_test@example.com",
    "Amit": "amit_test@example.com",
}
chores = ["Wash dishes", "Take out trash", "Vacuum living room"]


def assign_chores(people_dict, chore_list):
    shuffled_chores = chore_list[:]
    random.shuffle(shuffled_chores)
    return dict(zip(people_dict.keys(), shuffled_chores))


def send_chore_email(name, email_address, chore):
    msg = EmailMessage()
    msg["Subject"] = "Your Chore This Week"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email_address
    msg.set_content(f"Hi {name}, your assigned chore this week is: {chore}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        smtp.send_message(msg)

    print(f"Emailed {name} ({email_address}): {chore}")


def solve(send_real_emails=False):
    assignments = assign_chores(people, chores)

    for name, chore in assignments.items():
        email_address = people[name]
        print(f"{name} -> {chore}")

        if send_real_emails:
            send_chore_email(name, email_address, chore)


if __name__ == "__main__":
    solve(send_real_emails=False)  # flip to True once you trust it, with real emails