from turtle import Turtle
from position import Position
import random

RIGHT = 0

LEFT = 180

DOWN = 270

UP = 90

MOVE_DISTANCE = 20

START_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]

COLORS = ["green yellow", "brown", "light salmon"]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]

    def create_body(self):
        for i in range(0, len(START_POSITION)):
            pos = START_POSITION[i]
            new_seg = Turtle(shape="square")
            new_seg.color(COLORS[i % 3])
            new_seg.penup()
            new_seg.goto(pos)
            self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def head_pos(self):
        return Position(x=self.head.xcor(), y=self.head.ycor())

    def extend_body(self):
        new_seg = Turtle(shape="square")
        new_seg.color(COLORS[len(self.segments) % 3])
        new_seg.penup()
        new_seg.goto(self.tail.xcor(), self.tail.ycor())
        self.tail = new_seg
        self.segments.append(new_seg)

    @property
    def did_hit_body(self):
        # for i in range(4, len(self.segments)):
        #     print(f"{i} : {self.head.distance(self.segments[i])}")
        #     if self.head.distance(self.segments[i]) < 10:
        for segment in self.segments[1:]:
            # if segment == self.head:
            #     pass
            if self.head.distance(segment) < 10:
                return True
        return False

    def did_hit_wall(self, min_x, max_x, min_y, max_y):
        if self.head.xcor() < min_x or self.head.xcor() > max_x or self.head.ycor() < min_y or self.head.ycor() > max_y:
            return True
        return False



