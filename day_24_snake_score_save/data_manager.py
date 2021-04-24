# https://mark1002.github.io/2018/07/31/python-%E5%AF%A6%E7%8F%BE-singleton-%E6%A8%A1%E5%BC%8F/
# https://linuxize.com/post/python-check-if-file-exists/
# https://stackoverflow.com/a/61470282/9795114

import os.path


class DataManager:
    # instance
    __instance = None

    @staticmethod
    def get_instance():
        if DataManager.__instance is None:
            DataManager()
        return DataManager.__instance

    def __init__(self):
        if DataManager.__instance is not None:
            raise Exception('only one instance can exist')
        else:
            DataManager.__instance = self

    def save_score(self, highest_score):
        with open("highest_score.txt", mode="a") as f:
            f.seek(0)
            f.truncate()
            f.write(str(highest_score))

    @property
    def get_score(self):
        if os.path.isfile("highest_score.txt"):
            with open("highest_score.txt", mode="r") as f:
                score_text = f.readline().strip()
                return int(score_text)
        else:
            with open("highest_score.txt", mode="w") as f:
                f.write("0")
            return 0






