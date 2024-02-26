from enum import Enum

class GameState(Enum):

    NOT_STARTED = 0
    ROUND_DONE = 1
    GAME_OVER = 2
    ROUND_ACTIVE = 3
    def __init__(self):
        super.__init__()

        pass

    def on_key_press(self):
        pass


