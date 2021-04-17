from turtle import Turtle, Screen
import lane
from lane import Lane, Direction
from player import Player
from game_over import GameOver

OFFSET = 20
SCORE_SPACE = 60
LANE_SPACE = 30


class Field:

    def __init__(self, screen: Screen):
        self.screen = screen
        self.width = screen.window_width() - 2 * OFFSET
        self.height = screen.window_height() - 2 * OFFSET - SCORE_SPACE
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.lanes = []
        self.player = Player(min_x=-self.width/2,
                             max_x=self.width/2,
                             min_y=-self.height/2 + 10,
                             max_y=self.height/2 - 10)
        self.game_over = GameOver()

        self.__prepare_listener()
        self.__prepare_field()
        self.__prepare_lanes()
        self.__prepare_game_over()

    def __prepare_field(self):
        origin_x = -self.width / 2
        origin_y = -self.height/2
        self.turtle.penup()
        self.turtle.goto(x=origin_x, y=origin_y)

        # draw rectangle
        self.turtle.pendown()
        self.turtle.goto(x=-origin_x, y=origin_y)
        self.turtle.goto(x=-origin_x, y=-origin_y)
        self.turtle.goto(x=origin_x, y=-origin_y)
        self.turtle.goto(x=origin_x, y=origin_y)

    def __prepare_lanes(self):
        max_number_of_lane = int(self.height / (lane.MINIMUM_WIDTH + LANE_SPACE * 2)) - 1
        # print(max_number_of_lane)
        if max_number_of_lane <= 0:
            raise Exception("Your screen size is way too small")

        for i in range(1, max_number_of_lane + 1):
            origin = (float(-self.width / 2),
                      -self.height/2 + (lane.MINIMUM_WIDTH + LANE_SPACE * 2) * i)
            new_lane = Lane(origin, width=self.width, height=lane.MINIMUM_WIDTH + LANE_SPACE * 2,
                            should_draw_outline=False)
            if i % 2 == 0:
                new_lane.direction = Direction.RIGHT_TO_LEFT

            self.lanes.append(new_lane)

    def __prepare_listener(self):
        self.screen.listen()
        self.screen.onkey(self.player.go_up, "Up")
        self.screen.onkey(self.player.go_left, "Left")
        self.screen.onkey(self.player.go_right, "Right")
        self.screen.onkey(self.player.go_back, "Down")

    def __prepare_game_over(self):
        self.game_over.penup()
        self.game_over.goto(0, 0)

    def move_cars(self):
        for current_lane in self.lanes:
            current_lane.move_cars()

    def player_did_hit_by_car(self) -> bool:
        for current_lane in self.lanes:
            if current_lane.player_did_hit_by_car(self.player):
                return True
        return False

    @property
    def player_did_reach_top(self):
        return self.player.did_reach_top

    def reset_game(self):
        self.player.go_to_starting_pos()

    def set_up_scoreboard(self, turtle: Turtle):
        turtle.penup()
        turtle.goto(x=-self.width / 2, y=self.height / 2)

    def show_game_over(self):
        self.game_over.display_game_over()








