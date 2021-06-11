import smtplib
from datetime import datetime as dt
from secret import *
import random


def get_random_quote() -> str:
    with open("quotes.txt", mode="r") as f:
        quotes = f.readlines()
        print(quotes)
        return random.choice(quotes)


today = dt.now()
print(get_random_quote())
if today.weekday() == 4-1:
    with smtplib.SMTP(host=GMAIL_HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APPLICATION_PASSWORD)
        msg = f"Subject:Encouraging Quote\n\n{get_random_quote()}"
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_MAIL, msg=msg)


