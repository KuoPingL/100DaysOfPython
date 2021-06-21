import requests

BASE_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 25.0478
MY_LNG = 121.5318
KEY_SUNRISE = "sunrise"
KEY_SUNSET = "sunset"

# params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
#
# response = requests.get(BASE_URL, params)
# json = response.json()
#
# print(json)
#
# sunrise = json["results"]["sunrise"]
# sunrise = sunrise.split("T")[1].split("+")[0].split(":")
#
# print(sunrise)
#
# response.raise_for_status()


def request_sunrise_sunset_hour(gmt: int = 0) -> dict:
    params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
    response = requests.get(BASE_URL, params)

    if response.status_code != 200:
        raise Exception(f"Bad response from ISS API : {response.status_code}")

    if response.raise_for_status() == requests.HTTPError:
        raise Exception(f"Bad response from ISS API : {response.status_code}")

    json = response.json()
    sunrise = (int(json["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0]) + gmt) % 24
    sunset = (int(json["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0]) + gmt) % 24

    return {KEY_SUNRISE: sunrise, KEY_SUNSET: sunset}
