import requests
import json
from genders import Gender
import datetime

APPLICATION_ID = "32f2642f"
APPLICATION_KEYS = "40e0835418adaf6456670142292a1b9d"
SHEET_URL = "https://api.sheety.co/11696cf9e892c7615360e3f7d8057c80/100DaysPythonMyWorkouts/workouts"


class NutritionNix:

    BASE_URL = "https://trackapi.nutritionix.com"
    VERSION = "v2"

    @staticmethod
    def nl_exercise_url():
        return "/".join([NutritionNix.BASE_URL,
                         NutritionNix.VERSION,
                         "natural/exercise"])

    def __init__(self, app_id, app_key, gender: Gender, weight: float, height: float, age: int):
        self.x_app_id = app_id
        self.x_app_key = app_key
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age

    def post_exercise(self, nl_exercise: str) -> dict:
        url = NutritionNix.nl_exercise_url()
        try:
            headers = {"x-app-id": self.x_app_id,
                       "x-app-key": self.x_app_key,
                       "Content-Type": "application/json"}
            body = {"query": nl_exercise,
                    "gender": self.gender.name,
                    "weight_kg": self.weight,
                    "height_cm": self.height,
                    "age": self.age
                    }
            response = requests.post(url, json=body,  headers=headers)
            resp_json = response.json()
        except requests.HTTPError as e:
            print(f"post_exercise HTTP Error: {e}")
            return {}
        except json.JSONDecodeError as e:
            print(f"post_exercise JSON Error: {e}")
            return {}
        else:
            print(f"post_exercise response : {response.content}")
            return resp_json


class MySheety:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token

    def fetch_data_from_spreadsheet(self) -> dict:
        resp_json = None
        headers = {
            # "Authorization": f"Basic {self.token}"
            "Authorization": f"Bearer {self.token}"
        }

        try:
            response = requests.get(self.base_url, headers=headers)
            resp_json = response.json()
        except requests.HTTPError as e:
            print(f"fetch_data_from_spreadsheet HTTP Error: {e}")
        except json.JSONDecodeError as e:
            print(f"fetch_data_from_spreadsheet HTTP Error: {e}")
        else:
            print(f"fetch_data_from_spreadsheet : {response.content}")
        finally:
            if resp_json is None:
                resp_json = {}
            return resp_json

    def add_row(self, exercise: str, duration: float, calories: float,
                date_str: str = datetime.date.today().strftime("%d/%m/%Y"),
                time_str: float = 0.0,):
        resp_json = None
        # headers = {
        #     "Authorization": f"Basic {self.token}",
        #     "Content-Type": "application/json"
        # }

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        body = {
            "workout": {
                "date": date_str,
                "time": time_str,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        }

        try:
            response = requests.post(self.base_url, json=body, headers=headers)
            resp_json = response.json()
        except requests.HTTPError as e:
            print(f"add_row HTTP Error: {e}")
        except json.JSONDecodeError as e:
            print(f"add_row HTTP Error: {e}")
        else:
            print(f"add_row : {response.content}")
        finally:
            if resp_json is None:
                resp_json = {}
            return resp_json


nix = NutritionNix(app_id=APPLICATION_ID,
                   app_key=APPLICATION_KEYS,
                   gender=Gender.MALE,
                   height=168,
                   weight=85,
                   age=35)
# nix.post_exercise("I have swam for 10 hours")

nl_str = input("Tell me which exercise you did: ")
nix_json = nix.post_exercise(nl_str)

# sheety = MySheety(SHEET_URL, token="a3BsOjEyM2FiYw==")
sheety = MySheety(SHEET_URL, token="mklmklkljklll;k;lkokojjjknihiu")

for nix_data in nix_json["exercises"]:
    date = datetime.datetime.now()
    date_str = date.strftime("%d/%m/%Y")
    time = date.time()
    # time_str = ((time.hour + ((time.minute + (time.second / 60.0)) / 60.0)) / 24.0)
    time_str = datetime\
        .timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)\
        .total_seconds() / (60 * 60 * 24)
    exercise = nix_data["user_input"].title()
    duration = nix_data["duration_min"]
    calories = nix_data["nf_calories"]
    sheety.add_row(exercise, duration, calories, date_str, time_str)


print(sheety.fetch_data_from_spreadsheet())
