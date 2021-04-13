from turtle import Turtle, Screen
from game_types import GameTypes
from vector import Vector
from field import Field

MIN_VELOCITY = 10


class Ball(Turtle):
    def __init__(self, game_type: GameTypes = GameTypes.DEFAULT, field_height=0):
        super(Ball, self).__init__()
        self.color("white")
        self.penup()
        self.game_type = game_type
        if game_type is GameTypes.AIR_HOCKEY:
            self.shape(name="circle")
        else:
            self.shape(name="square")
            self.shapesize(stretch_wid=0.5)

        self.vector = Vector(init_vx=1, init_vy=0)
        self.velocity = MIN_VELOCITY
        self.min_y = -field_height / 2
        self.max_y = field_height / 2

    def reset_config(self):
        self.vector = Vector(init_vx=1, init_vy=1)
        self.velocity = MIN_VELOCITY
        self.goto(0, 0)

    def move(self):
        next_x = self.xcor() + self.vector.vx * self.velocity
        next_y = self.ycor() + self.vector.vy * self.velocity

        if next_y < 0 and next_y < self.min_y:
            next_y = self.min_y
        elif next_y > 0 and next_y > self.max_y:
            next_y = self.max_y

        self.goto(next_x, next_y)

    def bounce_off_from_top_bottom_wall(self, new_vector=Vector()):
        self.vector.add_vector(new_vector)
        self.vector = Vector(init_vx=self.vector.vx, init_vy=-self.vector.vy)

    def bounce_off_from_paddle(self, new_vector=Vector()):
        self.vector.add_vector(new_vector)
        self.vector = Vector(init_vx=-self.vector.vx, init_vy=self.vector.vy)

    def has_reached_top_or_bottom(self):
        extra_space = self.shapesize()[0] * 10/2
        if (self.ycor() > 0 and self.ycor() + extra_space >= self.max_y) or \
                (self.ycor() < 0 and self.ycor() - extra_space <= self.min_y):
            return True
        return False

    def has_reached_paddle(self, paddle: Turtle):
        max_distance = paddle.shapesize()[0] * 10 + self.shapesize()[0] * 10

        if self.distance(paddle) < max_distance:
            if self.xcor() > 0 and 0 < paddle.xcor() <= self.xcor():
                return True
            elif self.xcor() < 0 and self.xcor() <= paddle.xcor() < 0:
                return True
        return False

    def has_reached_goal(self, field: Field):
        goal_x = field.width / 2
        if self.xcor() >= goal_x or self.xcor() <= -goal_x:
            return True
        return False







