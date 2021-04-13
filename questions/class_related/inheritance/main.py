class Car:
    def __init__(self, name):
        self.name = name
        # Car.name = name

    def exclaim(self):
        print("I am a car")


class Yugo(Car):
    def exclaim(self):
        print("I am a cat")

    def needPush(self):
        print("A little help please")


a = Car("cat")
b = Yugo("car")
print(b.name)





