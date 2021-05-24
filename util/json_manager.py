import json


class JsonManager:
    def __init__(self, file_dir: str):
        self.file = file_dir

    def load(self) -> json:
        f = None
        try:
            f = open(self.file, mode="r")
        except FileNotFoundError or FileExistsError as e:
            f = open(self.file, mode="w")
            json.dump({}, fp=f, indent=4)
            f = open(self.file, mode="r")
        finally:
            print(f)
            data = json.load(fp=f)
            f.close()
            return data

    def update(self, new_data: dict):
        old_data = self.load()
        old_data.update(new_data)
        self.write(old_data)

    def write(self, new_data: dict):
        f = open(self.file, mode="w")
        json.dump(new_data, fp=f, indent=4)
        f.close()


