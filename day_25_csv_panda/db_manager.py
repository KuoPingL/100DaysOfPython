from weather import Weather
import pandas as pd

FILE = "weather_data.csv"
DAY_KEY = "day"
TEMP_KEY = "temp"
CON_KEY = "condition"


class DBManager:

    __instance = None

    @staticmethod
    def get_instance():
        if DBManager.__instance is None:
            # DBManager.__instance = DBManager()
            DBManager()
        return DBManager.__instance

    def __init__(self):
        if DBManager.__instance is not None:
            raise Exception('only one instance can exist')
        else:
            DBManager.__instance = self
            self.df = pd.read_csv(FILE)

    def get_weathers(self) -> [Weather]:
        data = []
        df = self.df
        for i in df.index:
            print(len(df.columns))
            day = df[DAY_KEY][i]
            temp = int(df[TEMP_KEY][i])
            condition = df[CON_KEY][i]
            data.append(Weather(day, temp, condition))

        return data

        # print(df.index)

    @property
    def get_average_temp(self):
        # return df[TEMP_KEY].mean()

        # or
        temp = self.df[TEMP_KEY].tolist()
        return sum(temp) / len(temp)

    @property
    def get_max_temp(self):
        # return self.df[TEMP_KEY].max()
        return self.df.temp.max()

    @property
    def get_max_temp_data(self):
        return self.df[self.df.temp == self.get_max_temp]
        # return self.df[self.df.temp == self.get_max_temp]

    @property
    def get_monday(self):
        return self.df[self.df.day == "Monday"]

