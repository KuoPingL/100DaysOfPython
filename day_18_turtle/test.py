# https://stackoverflow.com/questions/56528067/how-can-i-change-the-size-of-my-python-turtle-window

from turtle import Screen, Turtle

WIDTH, HEIGHT = 360, 360

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")

def scalePoint(n, start1, stop1, start2, stop2):
    return (n - start1) * (stop2 - start2) / (stop1 - start1)  + start2

screen.tracer(False)

for x in range(WIDTH):
    real = scalePoint(x, 0, WIDTH, -2, 2)

    for y in range(HEIGHT):

        imaginary = scalePoint(y, 0, HEIGHT, -2, 2)

        c = complex(real, imaginary)

        z = 0j

        color = 'pink'

        for _ in range(100):
            if abs(z) >= 16.0:
                break

            z = z * z + c
        else:
            color = 'black'

        turtle.goto(x, y)
        turtle.dot(1, color)

    screen.update()

screen.tracer(True)
screen.exitonclick()