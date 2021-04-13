from turtle import Turtle, Screen
import random

# raphael = Turtle()
is_race_on = False
screen = Screen()

user_bet = screen.textinput(title="Bet", prompt="Which turtle will win the race?")
colors = ['red', 'orange', 'blue', 'green', 'purple']

y_positions = [-70, -40, -10, 20, 50, 80]

turtles = []

for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=230, y=y_positions[i])
    turtles.append(t)

if user_bet:
    is_race_on = True

lt = Turtle()
lt.penup()
lt.goto(-230, -230)
lt.pendown()
lt.setheading(90)
lt.goto(-230, 230)

lt.penup()
lt.goto(230, -230)
lt.pendown()
lt.goto(230, 230)

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            if user_bet == t.pencolor():
                print("You Won")
            else:
                print("You Lose")
            is_race_on = False

    rand_dis = random.randint(0, 10)
    rand_t = random.choice(turtles)
    rand_t.forward(rand_dis)





screen.exitonclick()
