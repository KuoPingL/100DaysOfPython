from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
HEAD_LENGTH = 15
TAIL_LENGTH = 5


class Player(Turtle):
    def __init__(self, min_x, max_x, min_y, max_y):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.starting_pos = (0, min_y)
        self.finish_line = max_y
        self.width_limit = (min_x, max_x)
        self.goto(self.starting_pos)

    def go_up(self):
        if self.heading() != 90:
            self.setheading(90)
        else:
            final_y = self.ycor() + MOVE_DISTANCE
            print(final_y)
            print(self.finish_line)
            if final_y > self.finish_line - self.shapesize()[0] * 10:
                final_y = self.finish_line - self.shapesize()[0] * 10
            self.goto(self.xcor(), final_y)

    def go_back(self):
        if self.heading() != 270:
            self.setheading(270)
        else:
            final_y = self.ycor() - MOVE_DISTANCE
            if final_y < self.starting_pos[1]:
                final_y = self.starting_pos[1]
            self.goto(self.xcor(), final_y)

    def go_left(self):
        if self.heading() != 180:
            self.setheading(180)
        else:
            final_x = self.xcor() - MOVE_DISTANCE
            if final_x < self.width_limit[0]:
                final_x = self.width_limit[0]
            self.goto(final_x, self.ycor())

    def go_right(self):
        if self.heading() != 0:
            self.setheading(0)
        else:
            final_x = self.xcor() + MOVE_DISTANCE
            if final_x > self.width_limit[1]:
                final_x = self.width_limit[1]
            self.goto(final_x, self.ycor())

    @property
    def did_reach_top(self):
        return self.ycor() + HEAD_LENGTH >= self.finish_line

    def go_to_starting_pos(self):
        self.goto(self.starting_pos)
