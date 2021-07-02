import requests
import email.message
from twilio.rest import Client
import pandas

OPEN_WEATHER_API_KEY = "fbf9fea4ae1064d29c5a5ce72ef16510"

# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=6ee51981b465474485c5e33b0e6f537e

BASE_URL = "http://api.openweathermap.org/data/2.5/"
WEATHER_URL = BASE_URL + "weather"
ONE_CALL_URL = BASE_URL + "onecall"

LAT = 23.5000
LNG = 121.0000


def get_current_weather_for(city: str,
                            state_code: str = None,
                            country_code: str = None) -> dict:
    url = WEATHER_URL + f"?q={city}"
    if state_code:
        url += f",{state_code}"
    if country_code:
        url += f",{country_code}"
    url = append_app_id(url)
    response = requests.get(url=url)
    if response.raise_for_status() == requests.HTTPError:
        return {}
    return response.json()


def get_48_hour_weathers(lat: float,
                         lng: float,
                         *excludes: str) -> dict:
    url = ONE_CALL_URL + f"?lat={lat}&lon={lng}"
    if excludes:
        url += f"&exclude={','.join(excludes)}"
    url = append_app_id(url)
    print(url)
    response = requests.get(url=url)
    if response.raise_for_status() == requests.HTTPError:
        return {}
    return response.json()


def append_app_id(url: str) -> str:
    return url + f"&appid={OPEN_WEATHER_API_KEY}"


def send_warning():
    import os
    from twilio.rest import Client

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.getenv("OWM_API_KEY")
    auth_token = os.getenv("OWM_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    client.messages.create(
        body='Hi there',
        from_='+13607955332',
        to='+8860918756081')


data = get_48_hour_weathers(LAT, LNG, "current", "minutely", "daily")

first_12_data = [int(d["weather"][0]["id"]) < 700 for d in data["hourly"][:12]]
print(first_12_data)
print(True in first_12_data)

if True in first_12_data:
    send_warning()






