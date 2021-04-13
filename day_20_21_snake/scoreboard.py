from turtle import Turtle

FONT = ("Arial", 14, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.align_text(x, y)
        self.refresh()

    def align_text(self, x, y):
        self.penup()
        self.goto(x, y)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.refresh()

    def refresh(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def get_score(self):
        return self.score

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)




