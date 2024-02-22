from enum import Enum

class GameState(Enum):
    NOT_STARTED = 0
    ROUND_DONE = 0
    GAME_OVER = 0
    ROUND_ACTIVE = 0
    def __init__(self):
        super.__init__()

    def on_key_press(self):
        pass


