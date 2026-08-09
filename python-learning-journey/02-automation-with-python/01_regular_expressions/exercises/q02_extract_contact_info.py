"""
Question:
Write a program that scans a block of text using regex and pulls out
every phone number and email address it finds, printing them as a
clean list.

"""

import re


def extract_phone_numbers(text):
    phone_regex = re.compile(r"(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})")
    return phone_regex.findall(text)


def extract_emails(text):
    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    return email_regex.findall(text)


def solve(text):
    phones = extract_phone_numbers(text)
    emails = extract_emails(text)

    print("Phone numbers found:")
    for phone in phones:
        print(f"  {phone}")

    print("Emails found:")
    for email in emails:
        print(f"  {email}")

    return phones, emails


if __name__ == "__main__":
    sample_text = """
    Hi, you can reach Rahul at rahul.sharma@example.com or call 987-654-3210.
    For support, email support@company.com or call 123.456.7890.
    Alternate contact: 9876543210
    """
    solve(sample_text)