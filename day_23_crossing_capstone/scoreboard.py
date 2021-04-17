from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()

    def display_level(self, level):
        self.clear()
        self.write(f"LEVEL {level}", font=FONT, align=ALIGN)



