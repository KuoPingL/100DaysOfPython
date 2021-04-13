from turtle import Turtle, Screen
import random
import math
from my_math.lcm import lcm, gcd

leonardo_the_turtle = Turtle()

leonardo_the_turtle.shape("turtle")
leonardo_the_turtle.color('#285078', 'green')
# leonardo_the_turtle.pencolor('#fff')


# create screen
screen = Screen()
screen.colormode(255)


def draw_polygon(turtle: Turtle, sides, length):
    if sides < 2:
        sides = 3
    # turtle.begin_fill()
    # angle = float((sides - 2) * 180) / sides
    angle = 360 / sides  # this gives me a star
    for _ in range(sides):
        # turtle.right(180 - angle)
        turtle.forward(length)
        turtle.right(angle)
    # turtle.end_fill()


def draw_dashed_polygon(turtle: Turtle, sides, length, dash_per_line=3):
    if sides < 2:
        sides = 3
    angle = float((sides - 2) * 180) / sides

    for _ in range(sides):
        turtle.right(180 - angle)
        section = length / (dash_per_line * 2)
        for i in range(dash_per_line * 2):
            if i % 2 == 0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(section)


# draw_polygon(leonardo_the_turtle, 10, 100)
# draw_dashed_polygon(leonardo_the_turtle, 10, 100, 2)


def draw_multiple_polygon(turtle: Turtle, sides, length, count):
    draw_polygon(turtle, sides, length)
    turtle.left(360 / sides)
    turtle.forward(length)


# draw_multiple_polygon(leonardo_the_turtle, 10, 100, 3)


def hexagon(turtle: Turtle):
    for _ in range(6):
        turtle.forward(100)
        turtle.left(60)


def draw_multiple_hexagon():
    for _ in range(6):
        hexagon(leonardo_the_turtle)
        leonardo_the_turtle.forward(100)
        leonardo_the_turtle.right(60)


def draw_multiple_shapes():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    i = 3
    for _ in colours:
        leonardo_the_turtle.color(random.choice(colours))
        draw_polygon(leonardo_the_turtle, i, 100)
        i += 1


def turtle_go_left(length):
    leonardo_the_turtle.left(90)
    leonardo_the_turtle.forward(length)


def turtle_go_right(length):
    leonardo_the_turtle.right(90)
    leonardo_the_turtle.forward(length)


def random_color():
    # leonardo_the_turtle.pencolor(random.random(), random.random(), random.random())
    leonardo_the_turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


def display_random_walk(length=5, size=1):
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    leonardo_the_turtle.speed("fastest")
    leonardo_the_turtle.pensize(size)
    # directions = [lambda x: leonardo_the_turtle.forward(x),
    #               lambda x: turtle_go_left(x),
    #               lambda x: leonardo_the_turtle.back(x),
    #               lambda x: turtle_go_right(x)]
    #
    # # i = 0
    # # while i < 1000:
    # for _ in range(200):
    #     leonardo_the_turtle.color(random.choice(colours))
    #     random.choice(directions)(length)

    directions = [0, 90, 180, 270]
    for _ in range(200):
        # leonardo_the_turtle.color(random.choice(colours))
        random_color()
        # leonardo_the_turtle.pencolor()
        leonardo_the_turtle.right(random.choice(directions))
        leonardo_the_turtle.forward(length)


# display_random_walk(30, 5)

# =================
# SPIROGRAPH

def draw_simple_spirograph():
    step = 10
    for angle in range(0, 360 - step, step):
        random_color()
        leonardo_the_turtle.right(10)
        leonardo_the_turtle.circle(50)


def draw_circular_spirograph(inner_circle_radius=80, outer_circle_radius=105,
                             pen_location=40):
    if pen_location > inner_circle_radius:
        raise ValueError(f"pen_location ({pen_location}) should be "
                         f"less than inner_circle_radius({inner_circle_radius})")

    l = float(pen_location) / float(inner_circle_radius)
    k = float(inner_circle_radius) / float(outer_circle_radius)

    for angle in range(0, 360, 1):
        if angle == 0:
            leonardo_the_turtle.penup()
        else:
            leonardo_the_turtle.pendown()
        rad = float(angle) / (2 * math.pi)
        x = outer_circle_radius * ((1 - k) * math.cos(rad) + l * k * math.cos((1 - k) / k * rad))
        y = outer_circle_radius * ((1 - k) * math.sin(rad) - l * k * math.sin((1 - k) / k * rad))
        leonardo_the_turtle.goto(x, y)


def draw_circular_spirograph_with_k(k=1.1, outer_circle_radius=180,
                             pen_location=50):

    inner_circle_radius = k * float(outer_circle_radius)

    if pen_location > int(inner_circle_radius):
        raise ValueError(f"pen_location ({pen_location}) should be "
                         f"less than inner_circle_radius({inner_circle_radius})")

    l = float(pen_location) / float(inner_circle_radius)

    print(inner_circle_radius)
    print(outer_circle_radius)
    lcm_value = gcd(int(inner_circle_radius), int(outer_circle_radius))

    print(lcm_value)

    for angle in range(0, 360, 1):
        if angle == 0:
            leonardo_the_turtle.penup()
        else:
            leonardo_the_turtle.pendown()
        rad = float(angle) / (2 * math.pi)
        x = outer_circle_radius * ((1 - k) * math.cos(rad) + l * k * math.cos((1 - k) / k * rad))
        y = outer_circle_radius * ((1 - k) * math.sin(rad) - l * k * math.sin((1 - k) / k * rad))
        leonardo_the_turtle.goto(x, y)


leonardo_the_turtle.speed("fastest")
# draw_simple_spirograph()
draw_circular_spirograph()
# draw_circular_spirograph_with_k()
# screen.bgcolor('black')
screen.exitonclick()
