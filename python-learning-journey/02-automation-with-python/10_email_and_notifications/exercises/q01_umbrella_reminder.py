"""
Question:
Write a program that checks a weather API for today's forecast, and if
rain is expected, sends an email reminding to bring an umbrella.

"""

import os
import smtplib
import requests
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.environ.get("EMAIL_APP_PASSWORD")


def is_rain_expected(city="Hisar"):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    response.raise_for_status()
    data = response.json()

    chance_of_rain = int(data["weather"][0]["hourly"][4]["chanceofrain"])
    return chance_of_rain >= 50, chance_of_rain


def send_reminder_email(chance_of_rain):
    msg = EmailMessage()
    msg["Subject"] = "Umbrella Reminder"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content(f"Rain is expected today ({chance_of_rain}% chance) — bring an umbrella!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        smtp.send_message(msg)

    print("Reminder email sent.")


def solve():
    rain_expected, chance = is_rain_expected("Hisar")
    print(f"Chance of rain: {chance}%")

    if rain_expected:
        send_reminder_email(chance)
    else:
        print("No rain expected, no email sent.")


if __name__ == "__main__":
    solve()