##################### Extra Hard Starting Project ######################
import pandas as pd
from datetime import datetime as dt
import random
import smtplib
import sys

# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.insert(1,
                "/day_32_smtp/BirthdayWisher(Day32)start")

from secret import *


# dict comprehension
# new_dict = {new_key, new_value for (index, data_row) in data.iterrows()}
def note_dict_comprehension():
    data_frame = pd.read_csv("birthdays.csv")
    birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data_frame.iterrows()}
    print(birthday_dict)


# note_dict_comprehension()

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
class BirthdayPerson:
    def __init__(self, name, email):
        self.name = name
        self.email = email


def fetch_birthdayee() -> [BirthdayPerson]:
    today = dt.today()
    data_frame = pd.read_csv("birthdays.csv")
    print(data_frame.month)
    birthdayee = data_frame[data_frame["month"] == today.month]
    birthdayee = birthdayee[birthdayee.day == today.day].to_dict(orient="records")
    return {BirthdayPerson(name=person["name"], email=person["email"]) for person in birthdayee}


def fetch_birthday_dicts() -> [{}]:
    today = dt.today()
    data_frame = pd.read_csv("birthdays.csv")
    return [{"name": data_row["name"], "email": data_row.email} for (_, data_row) in data_frame.iterrows()
            if data_row.month == today.month and data_row.day == today.day]


print(fetch_birthday_dicts())


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def fetch_random_letter() -> str:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as f:
        return f.read()


# 4. Send the letter generated in step 3 to that person's email address.

birthday_people = fetch_birthdayee()
if len(birthday_people) > 0:
    letter = fetch_random_letter()
    for person in birthday_people:
        msg = f"FROM:abc\nTO: cbc Subject: Happy Birthday {person.name}\n\n{letter.replace('[NAME]', person.name)}"
        email = person.email
        with smtplib.SMTP(host=GMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_APPLICATION_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg)
