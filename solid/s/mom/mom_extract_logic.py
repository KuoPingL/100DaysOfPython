class Person:
    def __init__(self, name: str):
        self.name = name


class Cook(Person):
    def cook(self):
        print(f"{self.name} is Cooking")


class Feeder(Person):
    def feed_baby(self):
        print(f"{self.name} is Feeding Baby")

    def feed_cat(self):
        print(f"{self.name} is Feeding Cat")


class Worker(Person):
    def work(self):
        print(f"{self.name} is Working")


class Mom:
    def __init__(self, cook: Cook, feeder: Feeder, worker: Worker, name: str = "Mom"):
        self.name = name
        self.cook = cook
        self.feeder = feeder
        self.worker = worker

        self.cook.name = name
        self.feeder.name = name
        self.worker.name = name

    def cooking(self):
        self.cook.cook()

    def feed_baby(self):
        self.feeder.feed_baby()

    def work(self):
        self.worker.work()

    def feed_cat(self):
        self.feeder.feed_cat()

    # ... more activities












