from enum import Enum, auto


class GameStatus(Enum):
    IN_PROGRESS = auto()
    GAME_OVER   = auto()
    PLAY_AGAIN  = auto()
