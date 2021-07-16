import requests


class FlightSearch:
    def __init__(self, kiwi_api_key: str):
        assert not kiwi_api_key == ""
        self.kiwi_api_key = kiwi_api_key
        self.base_url = "https://tequila-api.kiwi.com"
        self.locale = "en-US"

    def fetch_iata_codes(self, cities: list[str]):
        try:
            headers = {"apikey": self.kiwi_api_key}
            requests.get(self.base_url)
        except requests.HTTPError as e:
            raise requests.HTTPError(f"{e}")






