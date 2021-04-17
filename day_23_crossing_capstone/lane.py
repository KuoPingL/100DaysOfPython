from car_manager import CarManager, MAXIMUM_CAR_LENGTH
from enum import Enum, auto
from turtle import Turtle
from player import HEAD_LENGTH, TAIL_LENGTH
import random

MOVE_DIS = 10
MINIMUM_WIDTH = 20


class Direction(Enum):
    LEFT_TO_RIGHT = auto()
    RIGHT_TO_LEFT = auto()


class Lane:
    def __init__(self, origin, width, height, direction=Direction.LEFT_TO_RIGHT, should_draw_outline=True):
        self.origin = origin
        self.width = width
        self.height = height
        self.cars = []
        self.direction = direction
        self.next_car_space = 0
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.should_draw_outline = should_draw_outline
        self.__draw_outline()

    def __draw_outline(self):
        if self.should_draw_outline:
            origin = self.origin
            width = self.width
            height = self.height
            self.turtle.penup()
            self.turtle.goto(origin)
            self.turtle.pendown()
            self.turtle.pencolor("red")
            self.turtle.goto(x=origin[0], y=origin[1] + height)
            self.turtle.goto(x=origin[0] + width, y=origin[1] + height)
            self.turtle.goto(x=origin[0] + width, y=origin[1])
            self.turtle.goto(origin)

    def __prepare_car(self):
        car = CarManager.generate_car(expected_height=MINIMUM_WIDTH)
        x = self.origin[0]
        y = self.origin[1]
        init_x = x - car.car_width / 2
        init_y = y + self.height / 2
        if self.direction is Direction.RIGHT_TO_LEFT:
            init_x = self.width / 2 + car.car_width / 2
        car.goto(x=init_x, y=init_y)
        self.cars.append(car)
        self.next_car_space = random.randint(MAXIMUM_CAR_LENGTH, MAXIMUM_CAR_LENGTH + 20) * MOVE_DIS

    def move_cars(self):

        if len(self.cars) == 0:
            self.__prepare_car()
        else:
            latest_car = self.cars[len(self.cars) - 1]
            if self.direction is Direction.RIGHT_TO_LEFT:
                if self.width / 2 - (latest_car.xcor() + latest_car.car_width/2) > self.next_car_space:
                    self.__prepare_car()
            else:
                if self.width / 2 - abs(latest_car.xcor() - latest_car.car_width/2) > self.next_car_space:
                    self.__prepare_car()

        for car in self.cars:
            new_x = car.xcor() + MOVE_DIS
            if self.direction is Direction.RIGHT_TO_LEFT:
                new_x = car.xcor() - MOVE_DIS
            car.goto(x=new_x, y=car.ycor())
            car.draw_cor()

        self.__remove_cars()

    def __remove_cars(self):
        final_cars = []
        for car in self.cars:
            if -self.width / 2 - car.car_width <= car.xcor() <= self.width / 2 + car.car_width:
                final_cars.append(car)
            else:
                car.clear_all()
        self.cars.clear()
        self.cars = final_cars

    def player_did_hit_by_car(self, player: Turtle):
        player_top = player.shapesize()[1] * 10
        player_bottom = player.shapesize()[1] * 10
        player_left = player.shapesize()[1] * 10
        player_right = player.shapesize()[1] * 10
        if player.heading() == 0:
            player_right += HEAD_LENGTH
            player_left += TAIL_LENGTH
        if player.heading() == 180:
            player_right += TAIL_LENGTH
            player_left += HEAD_LENGTH
        if player.heading() == 90:
            player_top += HEAD_LENGTH
            player_bottom += TAIL_LENGTH
        if player.heading() == 270:
            player_top += TAIL_LENGTH
            player_bottom += HEAD_LENGTH

        for car in self.cars:
            min_x = car.xcor() - car.car_width / 2
            max_x = car.xcor() + car.car_width / 2
            min_y = car.ycor() - car.shapesize()[0] * 10 / 2
            max_y = car.ycor() + car.shapesize()[0] * 10 / 2

            if (min_x <= player.xcor() + player_right <= max_x or min_x <= player.xcor() - player_left <= max_x) \
                    and (min_y <= player.ycor() + player_top <= max_y
                         or min_y <= player.ycor() - player_bottom <= max_y) or \
                    (min_x <= player.xcor() <= max_x and min_y <= player.ycor() <= max_y):
                return True



