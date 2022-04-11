# --------------------------------------------------------
# - RoboBrisca
# - Bot1 for first phase of Robobrisca competition
# - It is just a RandomPlayer
# --------------------------------------------------------
import random

from Players.Player import Player


# ---------------------------------------------------------------------------
# Randomly selects one action from the list of possible actions
# ---------------------------------------------------------------------------
class Bot1(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        return random.choice(list_actions)

    def __str__(self):
        return "Bot1"
