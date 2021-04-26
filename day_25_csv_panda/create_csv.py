import pandas as pd


def create_csv_v1():
    data_dict = {
        "student": ["Ann", "Jane", "Joe"],
        "score": [80, 70, 60]
    }
    data = pd.DataFrame(data_dict)
    data.to_csv("create_csv_v1.csv")


def create_csv_v2():
    data = pd.DataFrame()
    data["student"] = ["Ann", "Jane", "Joe"]
    data["score"] = [80, 70, 60]
    data.to_csv("create_csv_v2.csv")

