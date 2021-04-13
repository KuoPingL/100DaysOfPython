from turtle import Turtle, Screen
from game_types import GameTypes
from paddle import Paddle
from scoreboard import Scoreboard

NUMBER_OF_DASHES = 41
OFFSET = 40


class Field(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.pensize(2)
        self.speed("fastest")
        self.screen = screen
        self.height = self.screen.window_height() - OFFSET
        self.width = self.screen.window_width() - OFFSET

        print(self.screen.window_height())
        print(self.height)

    def prepare_field(self, game_types: GameTypes):
        self.screen.setup(width=self.screen.window_width() + OFFSET, height=self.screen.window_height() + OFFSET)
        self.screen.bgcolor("black")

        self.__draw_outline()
        from_x = 0
        from_y = -self.height / 2
        self.__draw_center_line(from_x, from_y, -from_y, game_types)

    def setup_paddles(self, paddle_a: Paddle, paddle_b: Paddle):
        x = self.width / 2
        y = self.height / 2
        print(y)
        paddle_a.prepare(x=-x, min_y=-y, max_y=y)
        paddle_b.prepare(x=x, min_y=-y, max_y=y)

    def setup_scoreboard(self, scoreboard: Scoreboard):
        scoreboard.set_lplayer_score_location(-self.width/4, self.height/4)
        scoreboard.set_rplayer_score_location(self.width/4, self.height/4)

    def __draw_outline(self):
        self.goto(self.width / 2, self.height / 2)
        self.pendown()
        self.goto(-self.width / 2, self.height / 2)
        self.goto(-self.width / 2, -self.height / 2)
        self.goto(self.width / 2, -self.height / 2)
        self.goto(self.width / 2, self.height / 2)
        self.penup()

    def __draw_center_line(self, from_x, from_y, to_y, game_types=GameTypes.DEFAULT):
        self.penup()
        self.goto(from_x, from_y)

        if game_types is GameTypes.DEFAULT:
            dashed_seg_length = abs(from_y - to_y) / (NUMBER_OF_DASHES + NUMBER_OF_DASHES - 1)
            for i in range(1, NUMBER_OF_DASHES * 2):
                if i % 2 == 0:
                    self.penup()
                else:
                    self.pendown()
                self.goto(from_x, from_y + i * dashed_seg_length)

        elif game_types is GameTypes.AIR_HOCKEY:
            self.pendown()
            self.goto(from_x, to_y)



