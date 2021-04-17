from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"


class GameOver(Turtle):
    def __init__(self):
        super(GameOver, self).__init__()
        self.hideturtle()

    def display_game_over(self):
        self.clear()
        self.write("Game Over", align=ALIGN, font=FONT)