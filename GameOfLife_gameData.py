import numpy as np

class GameState:
    def __init__(self, initial_state):
        self.current_state = np.array(initial_state)