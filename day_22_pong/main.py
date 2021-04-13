from turtle import Turtle, Screen
from field import Field, OFFSET
from game_types import GameTypes
from paddle import Paddle
from scoreboard import Scoreboard, Player
from ball import Ball
from vector import Vector
import time
import tkinter as tk
import tkinter.font as tk_font

WIDTH = 800
HEIGHT = 600

# root = tk.Tk()
# print(tk_font.families())
# print(tk_font.names())

screen = Screen()
screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT)
field = Field(screen=screen)
ball = Ball(field_height=field.height)


field.prepare_field(GameTypes.DEFAULT)

paddle_a = Paddle()
paddle_b = Paddle()
field.setup_paddles(paddle_a=paddle_a, paddle_b=paddle_b)

scoreboard = Scoreboard(screen=screen)
field.setup_scoreboard(scoreboard)

screen.listen()
screen.onkey(paddle_b.move_up, key="Up")
screen.onkey(paddle_b.move_down, key="Down")

screen.onkey(paddle_a.move_up, key="w")
screen.onkey(paddle_a.move_down, key="s")

is_game_over = False
paddle_a_did_hit_ball = False
paddle_b_did_hit_ball = False
paddle_y_when_ball_is_hit = 0


def record_data_when_ball_hit_paddle(player: Player):
    global paddle_a_did_hit_ball, paddle_b_did_hit_ball, paddle_y_when_ball_is_hit, paddle_a, paddle_b
    if player is Player.PLAYER_A:
        paddle_y_when_ball_is_hit = paddle_a.ycor()
        paddle_a_did_hit_ball = True
    else:
        paddle_y_when_ball_is_hit = paddle_b.ycor()
        paddle_a_did_hit_ball = True


def change_ball_vector_based_on_paddle(paddle: Turtle):
    new_vy = 1

    # the ball is moving along x
    if ball.vector.vy == 0:
        if paddle.ycor() < paddle_y_when_ball_is_hit:
            new_vy = -1
    else:
        if paddle.ycor() > paddle_y_when_ball_is_hit and ball.vector.vy < 0 or \
                paddle.ycor() < paddle_y_when_ball_is_hit and ball.vector.vy > 0:
            # paddle is moving in the opposite direction of ball
            if abs(ball.vector.vy) > 1:
                # slow down the ball
                if ball.vector.vy < 0:
                    new_vy = 1
                else:
                    new_vy = -1
            else:
                # change direction of the ball vector.vy
                if ball.vector.vy < 0:
                    new_vy = -ball.vector.vy + 1
                else:
                    new_vy = -ball.vector.vy - 1

        else:
            # paddle is moving in the same direction of ball
            if ball.vector.vy < 0:
                new_vy = -1

    ball.vector.add_vector(Vector(init_vx=0, init_vy=new_vy))


while not is_game_over:
    time.sleep(0.1)
    screen.update()
    # paddle_b.move_as_ai()

    # check if paddle responsible for hitting the ball has moved
    if paddle_a_did_hit_ball and paddle_a.ycor() != paddle_y_when_ball_is_hit:
        change_ball_vector_based_on_paddle(paddle=paddle_a)
    elif paddle_b_did_hit_ball and paddle_b.ycor() != paddle_y_when_ball_is_hit:
        change_ball_vector_based_on_paddle(paddle=paddle_b)

    paddle_a_did_hit_ball = False
    paddle_b_did_hit_ball = False

    ball.move()

    if ball.has_reached_top_or_bottom():
        ball.bounce_off_from_top_bottom_wall()

    elif ball.has_reached_paddle(paddle_a):
        ball.bounce_off_from_paddle()
        record_data_when_ball_hit_paddle(Player.PLAYER_A)

    elif ball.has_reached_paddle(paddle_b):
        ball.bounce_off_from_paddle()
        record_data_when_ball_hit_paddle(Player.PLAYER_B)

    elif ball.has_reached_goal(field):

        if ball.xcor() > 0:
            scoreboard.inc_score(player=Player.PLAYER_B)
        else:
            scoreboard.inc_score(player=Player.PLAYER_A)
        ball.reset_config()


screen.exitonclick()
