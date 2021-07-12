from actions import Fight, Defense, Magic


class Character:
    def __init__(self, name):
        self.name = name


class Fighter(Character, Fight):
    def fight(self):
        print(f"Fighter {self.name} Fighting")


class Defender(Character, Defense):
    def defense(self):
        print(f"Defensor {self.name} Defensing")


class Magician(Character, Magic):
    def cast_spell(self):
        print(f"Magician {self.name} Casting Spell")


