# Sending Email, Texts & Push Notifications

**Source:** Book Ch.20

## Concepts covered
- The `smtplib` module for sending email via SMTP
- App passwords for Gmail/other providers (since regular passwords are blocked for this)
- Building an email message with `email.message.EmailMessage`
- Combining email sending with data from other sources (weather APIs, files, etc.)
- Basic idea of webhooks/push notifications as an alternative to email

## My Notes
`smtplib` connects to an email provider's SMTP server and sends a message the same way
a normal email client would, just done in code. Most providers (like Gmail) block plain
password login for this and require a separate "app password" generated in account
security settings — a common first stumbling block. This topic is really about
*triggering* an email from some other condition (a file check, an API result, a
schedule) rather than email-sending being the hard part itself.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Umbrella Reminder | ⬜ |
| 2 | Random Chore Assignment Emailer | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).