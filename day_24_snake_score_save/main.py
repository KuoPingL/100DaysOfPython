from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


WIDTH = 600
HEIGHT = 600

WALL_W = WIDTH - 60
WALL_H = HEIGHT - 60

screen = Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Eater")

outline = Turtle()
outline.color("white")
outline.pencolor("white")
outline.penup()
outline.goto(WALL_W / 2, -WALL_H/2)
outline.pendown()
outline.goto(WALL_W / 2, WALL_H / 2)
outline.goto(-WALL_W / 2, WALL_H / 2)
outline.goto(-WALL_W / 2, -WALL_H / 2)
outline.goto(WALL_W / 2, -WALL_H / 2)

body = []

is_game_on = True
screen.tracer(0)


def create_new_body():
    for i in range(3):
        t = Turtle(shape="square")
        t.fillcolor("white")
        t.color("white")
        t.penup()
        t.goto(-i * 20, 0)
        body.append(t)


def move_snake():
    while is_game_on:
        screen.update()
        time.sleep(0.1)

        for i in range(len(body) - 1, 0, -1):
            print(i)
            current_t = body[i]
            new_x = body[i - 1].xcor()
            new_y = body[i - 1].ycor()
            current_t.goto(new_x, new_y)

        # body[1].goto(body[0].xcor(), body[0].ycor())
        body[0].left(90)
        body[0].forward(20)


# create_new_body()
snake = Snake()
food = Food()
food.refresh(area_x=WALL_W, area_y=WALL_H)
scoreboard = Scoreboard(0, HEIGHT / 2.0 - 20)
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if int(snake.head_pos().x) == int(food.pos().x) and int(snake.head_pos().y) == int(food.pos().y):
    if snake.head.distance(food) < 15:
        food.refresh(area_x=WALL_W, area_y=WALL_H)
        snake.extend_body()
        scoreboard.inc_score()

    if snake.did_hit_body or snake.did_hit_wall(min_x=-WALL_W/2, max_x=WALL_W/2, min_y=-WALL_H/2, max_y=WALL_H/2):
        # is_game_on = False
        scoreboard.reset_scoreboard()
        snake.reset()
# move_snake()

screen.exitonclick()
