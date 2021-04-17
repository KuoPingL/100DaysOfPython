from turtle import Turtle, Screen
import time
from field import Field
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

is_game_on = True
level = 1

field = Field(screen)

scoreboard = Scoreboard()
field.set_up_scoreboard(scoreboard)
scoreboard.display_level(level=level)

while is_game_on:
    time.sleep(0.1 / level)
    screen.update()

    if field.player_did_hit_by_car():
        field.show_game_over()
        is_game_on = False

    if field.player_did_reach_top:
        # next level
        field.reset_game()
        level += 1
        scoreboard.display_level(level)

    field.move_cars()

screen.exitonclick()

