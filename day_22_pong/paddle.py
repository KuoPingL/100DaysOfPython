from turtle import Turtle, Screen
from enum import Enum, unique


@unique
class PaddleDirection(Enum):
    UP = 1
    DOWN = 2


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.x = 0
        self.min_y = 0
        self.max_y = 0
        self.auto_direction = PaddleDirection.UP

    def prepare(self, x, min_y, max_y):
        self.min_y = min_y
        self.max_y = max_y
        self.shape(name="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        real_x = x - self.shapesize()[1] * 10 - 20
        if x < 0:
            real_x = x + self.shapesize()[1] * 10 + 20
        self.x = real_x
        self.goto(real_x, 0)
        self.showturtle()

    def move_as_ai(self):
        self.speed("slow")

        expected_y = self.__get_valid_y_for_ai()

        next_y = self.__get_valid_y(expected_y)

        if next_y != expected_y:
            if self.auto_direction is PaddleDirection.UP:
                self.auto_direction = PaddleDirection.DOWN
            else:
                self.auto_direction = PaddleDirection.UP
            expected_y = self.__get_valid_y_for_ai()

        self.goto(self.x, expected_y)

        # 以下的是錯誤的寫法，由於 while 會一直跑，所以 onkey 變成無效
        # if next_y != expected_y:
        #     # the paddle has reached the end
        #     self.goto(self.x, self.ycor() - self.shapesize()[0] * 10)
        # else:
        #     self.goto(self.x, expected_y)

        # while True:
        #     self.goto(self.x, self.min_y + self.shapesize()[0] * 10)
        #     self.goto(self.x, self.max_y - self.shapesize()[0] * 10)

    def __get_valid_y_for_ai(self):
        if self.auto_direction is PaddleDirection.UP:
            return self.ycor() + self.shapesize()[0] * 10
        else:
            return self.ycor() - self.shapesize()[0] * 10

    def move_up(self):

        next_y = self.__get_valid_y(self.pos()[1] + self.max_y / 10)  # self.shapesize()[0] * 10 * 0.2)

        self.goto(self.x, next_y)

    def move_down(self):

        next_y = self.__get_valid_y(self.pos()[1] - self.max_y / 10)  # self.shapesize()[0] * 10 * 0.2)

        self.goto(self.x, next_y)

    def __get_valid_y(self, next_y):
        if next_y + self.shapesize()[0] * 10 >= self.max_y or next_y - self.shapesize()[0] * 10 <= self.min_y:
            return self.pos()[1]
        return next_y






