import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "hastonkira@gmail.com"
EMAIL_Password = os.environ.get("Email_Password")


def send_cbb_email(to, subject, message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg.set_content(message)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_Password)
        smtp.send_message(msg)
