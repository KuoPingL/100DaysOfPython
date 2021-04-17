from car import Car
import random

STARTING_MOVING_DIS = 5
MOVE_INCREMENT = 10
MAXIMUM_CAR_LENGTH = 8


class CarManager:

    @staticmethod
    def generate_car(expected_height) -> Car:
        return Car((random.randint(30, 255), random.randint(30, 255), random.randint(30, 255)),
                   stretch_wid=int(expected_height/10), stretch_len=random.randint(3, MAXIMUM_CAR_LENGTH))






