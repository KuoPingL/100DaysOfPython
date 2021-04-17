from turtle import Turtle, Screen
import random


class Car(Turtle):
    # stretch_wid = height ratio
    # stretch_len = width ratio
    def __init__(self, color, stretch_wid, stretch_len):
        super(Car, self).__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=stretch_len, stretch_wid=stretch_wid)
        self.getscreen().colormode(255)
        self.color(color)
        self.should_show_cor = False
        self.painter = Turtle()
        self.painter.hideturtle()
        self.painter.penup()

    @property
    def car_width(self):
        return self.shapesize()[1] * 10

    @property
    def car_height(self):
        return self.shapesize()[0] * 10

    def draw_cor(self):
        if self.should_show_cor:
            self.painter.clear()
            self.painter.goto(self.xcor(), self.ycor())
            self.painter.write(f"({self.xcor()}, {self.ycor()})")

    def clear_all(self):
        self.clear()
        self.hideturtle()
        self.should_show_cor = False
        self.painter.clear()


