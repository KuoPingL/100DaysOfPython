import requests
import json as json
from html import unescape
import os.path


class QuestionsFetcher:
    BASE_URL = "https://opentdb.com/api.php?amount=10&type=boolean"

    @classmethod
    def prepare_10_questions(cls) -> list:
        response = requests.get(QuestionsFetcher.BASE_URL)
        response.raise_for_status()
        get_json = response.json()

        data = get_json['results']
        for d in data:
            d["question"] = unescape(d["question"])

        # with open("data.py"), open("data.py", mode="w") as f:
        #     final_text = f"question_data = {json.dumps(data, indent=4)}"
        #     f.write(final_text)
        return data
