import math

from Game.ForwardModel import ForwardModel
from Game.Heuristic import Heuristic
from Players.Player import Player


class OSLAPlayer(Player):
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = Heuristic()

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
        return "OSLAPlayer"
