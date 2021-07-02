import pandas as pd

SQUIRREL_DATA = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
FUR_COLOR = "Primary Fur Color"


# Singleton
class SquirrelDBManager:

    __instance = None

    @staticmethod
    def get_instance():
        if SquirrelDBManager.__instance is None:
            SquirrelDBManager()
        return SquirrelDBManager.__instance

    def __init__(self):
        if SquirrelDBManager.__instance is not None:
            raise Exception("only one instance can exist")
        else:
            SquirrelDBManager.__instance = self
            self.df = pd.read_csv(SQUIRREL_DATA)
            print(self.find_primary_fur_colors())

    def find_primary_fur_colors(self):
        result = set(self.df[FUR_COLOR].tolist())
        # print(result)
        # for value in result:
        #     print(type(value))
        # https://stackoverflow.com/a/53346628/9795114
        # https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.notna.html
        # This function takes a scalar or array-like object and indictates whether values are valid
        # (not missing, which is NaN in numeric arrays, None or NaN in object arrays, NaT in datetime like).
        result = {x for x in result if pd.notna(x)}
        return sorted(result)

    def create_csv_for_fur_colors(self):
        furs = self.find_primary_fur_colors()
        fur_counts = []
        for fur in furs:
            print(fur)
            fur_data = self.df[self.df[FUR_COLOR] == fur]
            fur_count = fur_data.shape[0]
            fur_counts.append(fur_count)

        data = pd.DataFrame({FUR_COLOR: furs, "counts": fur_counts})
        data.to_csv("fur_static.csv")












