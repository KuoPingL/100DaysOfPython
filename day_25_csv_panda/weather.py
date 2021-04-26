class Weather:
    __slots__ = ("day", "temp", "condition")

    def __init__(self, day, temp, condition):
        self.day = day
        self.temp = temp
        self.condition = condition
