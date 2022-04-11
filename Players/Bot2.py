# --------------------------------------------------------
# - RoboBrisca
# - Bot2 for first phase of Robobrisca competition
# - It is a One Looking ahead player
# - It use a smarter heuristic than the default one
# --------------------------------------------------------
import math

from Game.ForwardModel import ForwardModel
from Players.MyHeuristic import MyHeuristic
from Players.Player import Player


class Bot2(Player):
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = MyHeuristic()

    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        best_value = -math.inf
        best_action = None
        for action in list_actions:
            new_obs = observation.clone()
            value = self.forward_model.play(new_obs, action, self.heuristic)
            if value >= best_value:
                best_action = action
                best_value = value
        return best_action

    def __str__(self):
        return "Bot2"
