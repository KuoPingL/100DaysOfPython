from turtle import Turtle, Screen
from enum import Enum, unique


@unique
class Player(Enum):
    PLAYER_A = 1
    PLAYER_B = 2


FONT = ("Courier", 80, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self, screen: Screen):
        super(Scoreboard, self).__init__()
        self.speed("fastest")
        self.color("white")
        self.playerAScore = 0
        self.playerBScore = 0
        self.hideturtle()
        self.playerALocation = (-screen.window_width() / 2, screen.window_height() / 2)
        self.playerBLocation = (-screen.window_width() / 2, screen.window_height() / 2)
        self.__display_score()

    def inc_score(self, player: Player):
        if player is Player.PLAYER_A:
            self.playerAScore += 1
        else:
            self.playerBScore += 1
        self.__display_score()

    def new_game(self):
        self.playerAScore = 0
        self.playerBScore = 0
        self.__display_score()

    def set_lplayer_score_location(self, *loc):
        self.playerALocation = loc
        self.__display_score()

    def set_rplayer_score_location(self, *loc):
        self.playerBLocation = loc
        self.__display_score()

    def __display_score(self):
        self.clear()
        self.penup()
        self.goto(self.playerALocation)
        self.write(self.playerAScore, align=ALIGN, font=FONT)
        self.goto(self.playerBLocation)
        self.write(self.playerBScore, align=ALIGN, font=FONT)







