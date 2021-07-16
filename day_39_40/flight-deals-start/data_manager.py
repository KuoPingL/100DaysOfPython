import requests
import json


class DataManager:

    def __init__(self, end_point: str, sheet_name: str, bearer=None, basic=None):
        if end_point.startswith("/"):
            end_point = end_point.replace("/", "", 1)
        self.base_url = "/".join(["https://api.sheety.co", end_point])



        self.headers = {}
        if not (bearer is None):
            self.headers = {"Authorization": f"Bearer {bearer}"}
        elif not (basic is None):
            self.headers = {"Authorization": f"Basic {basic}"}

        self.sheet_name = sheet_name

    def get_google_sheet(self):
        try:
            response = requests.get(self.base_url, headers=self.headers)
            resp_json = response.json()
        except requests.HTTPError as e:
            raise requests.HTTPError(f"DataManager => get_google_sheet: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"DataManager => get_google_sheet: JSON ERROR {e}")
        else:
            data = resp_json[self.sheet_name]

        print(data)

        # if data[0]["iataCode"] == "":
        #
        # else:
        #     return data

    # def _fetch_iata(self):

d = DataManager("11696cf9e892c7615360e3f7d8057c80/flightDeals/prices",
                bearer="FlightTrip",
                sheet_name="prices")
d.get_google_sheet()


