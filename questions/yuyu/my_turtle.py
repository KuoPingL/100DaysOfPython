from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, shape):
        super(MyTurtle, self).__init__(shape=shape)
        self.shape("square")



