from turtle import Turtle, Screen, mainloop, TurtleScreen

michael = Turtle()
screen = Screen()


def print_something():
    print("PRINT")


def forward():
    michael.forward(10)


screen.onkeyrelease(forward, "w")
screen.onkeyrelease(lambda: michael.back(10), "s")
screen.onkeyrelease(lambda: michael.right(2), "d")
screen.onkeyrelease(lambda: michael.left(2), "a")


def clear():
    michael.clear()
    michael.penup()
    # michael.goto(0, 0)
    # michael.setheading(0)
    michael.home()
    michael.pendown()


screen.onkeyrelease(clear, "c")

screen.listen()

mainloop()

