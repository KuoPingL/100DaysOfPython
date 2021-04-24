from turtle import Turtle
from data_manager import DataManager

FONT = ("Arial", 14, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.high_score = DataManager.get_instance().get_score
        self.color("white")
        self.hideturtle()
        self.align_text(x, y)
        self.refresh()

    def align_text(self, x, y):
        self.penup()
        self.goto(x, y)

    def inc_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def get_score(self):
        return self.score

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        DataManager.get_instance().save_score(self.high_score)
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)




