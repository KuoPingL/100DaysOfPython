class Animal:
    def __init__(self, animal_name: str):
        self.name = animal_name

    def bite(self):
        print(f"{self.name} Bite")

    def walk(self):
        print(f"{self.name} Walking")

    # def fly(self):
    #     print(f"{self.name} Flying")


class Bird(Animal):
    def fly(self):
        print(f"{self.name} Flying")





