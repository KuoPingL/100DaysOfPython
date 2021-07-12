from action_engin import ActionEngine


class Character:
    def __init__(self, name):
        self.name = name


class Fighter(Character, ActionEngine):
    def fight(self):
        print(f"Fighter {self.name} Fighting")

    def defense(self): pass

    def cast_spell(self): pass


class Defensor(Character, ActionEngine):
    def fight(self): pass

    def defense(self):
        print(f"Defensor {self.name} Defensing")

    def cast_spell(self): pass


class Magician(Character, ActionEngine):
    def fight(self): pass

    def defense(self): pass

    def cast_spell(self):
        print(f"Magician {self.name} Casting Spell")


