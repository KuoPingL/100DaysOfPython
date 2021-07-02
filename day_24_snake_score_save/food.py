from turtle import Turtle
from position import Position
import random


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.create_food()
        self.speed("fastest")

    def create_food(self):
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self, area_x, area_y):
        new_x = random.randint(-area_x/2.0 + 20, area_x/2.0 - 20)
        new_y = random.randint(-area_y/2.0 + 20, area_y/2.0 - 20)
        self.goto(new_x, new_y)
        print(f"FOOD LOC = {self.pos()}")

    def pos(self):
        return Position(x=self.xcor(), y=self.ycor())



