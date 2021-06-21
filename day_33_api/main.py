import requests
from datetime import datetime
from day_33_api.sunset_sunrise_api.sun_dial \
    import MY_LNG, MY_LAT, request_sunrise_sunset_hour, KEY_SUNRISE, KEY_SUNSET
import smtplib
import time
import json as j
import sys
sys.path.insert(1,
                "../day_32_smtp/BirthdayWisher(Day32)start")

from secret import *

JSON_KEY_POSITION = "iss_position"
JSON_KEY_TIMESTAMP = "timestamp"
JSON_KEY_LNG = "longitude"
JSON_KEY_LAT = "latitude"
JSON_KEY_MESSAGE = "message"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# print(isinstance(response.json(), dict))
#
# if response.status_code != 200:
#     raise Exception(f"Bad response from ISS API : {response.status_code}")
#
# if response.raise_for_status() == requests.HTTPError:
#     raise Exception(f"Bad response from ISS API : {response.status_code}")
#
# json = response.json()
# lng = float(json[JSON_KEY_POSITION][JSON_KEY_LNG])
# lat = float(json[JSON_KEY_POSITION][JSON_KEY_LAT])
#
# print(lng)

# if ISS is close to my current location
# and it is currently dark
# Then send me an email to tell me to look up
# Bonus: Run every 60 seconds

DELTA = 5


def request_data(tag: int = 0):
    print(f"=================== REQUEST_DATA : tag = {tag})")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    if response.status_code != 200:
        raise Exception(f"Bad response from ISS API : {response.status_code}")
    if response.raise_for_status() == requests.HTTPError:
        raise Exception(f"Bad response from ISS API : {response.status_code}")
    print(f"DONE REQUEST_DATA : tag = {tag}) ===================")
    return response.json()


def is_above_me(json: dict):
    lng = float(json[JSON_KEY_POSITION][JSON_KEY_LNG])
    lat = float(json[JSON_KEY_POSITION][JSON_KEY_LAT])
    return ((lat + DELTA) >= MY_LAT >= (lat - DELTA)) and \
           ((lng + DELTA) >= MY_LNG >= (lng - DELTA))


def is_at_night():
    current_hour = int(str(datetime.now()).split(" ")[1].split(".")[0].split(":")[0])
    sun_hour_dict = request_sunrise_sunset_hour(gmt=8)
    return current_hour >= sun_hour_dict[KEY_SUNSET]


while True:
    # fetch new data
    json = request_data()

    if is_above_me(json) and is_at_night():
        # send email
        with smtplib.SMTP(host="smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_APPLICATION_PASSWORD)
            msg = f"FROM:abc\nTO: cbc \nSubject: Here comes the ISS"
            FROM = MY_EMAIL
            TO = MY_EMAIL
            conn.sendmail(from_addr=FROM, to_addrs=TO, msg=msg)
    time.sleep(60)

