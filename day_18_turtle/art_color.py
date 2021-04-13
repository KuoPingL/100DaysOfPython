import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("image.jpg", 6)
print(colors)

rgbs = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgbs.append((r, g, b))

print(rgbs)


screen = Screen()
WIDTH = 360
HEIGHT = 360
screen.setup(WIDTH, HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.colormode(255)

leonardo = Turtle(shape="turtle")

def generate_25_dots_with_5_per_line():
    # 5 dots per line
    # default is pointing north, turn it to east
    leonardo.right(90)

    overall_height = screen.canvheight.real
    overall_width = screen.canvwidth.real


number_of_lines = int(input("How many number of lines do you want to draw? "))
number_of_dots_per_line = int(input("How many number of dots per line? "))

dot_size = 10
v_spacing = (screen.window_height()) / (number_of_lines + 1)
h_spacing = (screen.window_width()) / (number_of_dots_per_line + 1)

for line in range(1, number_of_lines + 1):
    y = line * v_spacing
    for dot in range(1, number_of_dots_per_line + 1):
        x = dot * h_spacing
        leonardo.penup()
        leonardo.goto(x, y)
        leonardo.pendown()
        leonardo.dot(10, random.choice(rgbs))

print(leonardo.shapesize())

screen.exitonclick()




