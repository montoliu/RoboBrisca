# --------------------------------------------------------
# - RoboBrisca
# - Bot3 for first phase of Robobrisca competition
# - It is a N-times Turn Looking ahead player, N is a number depending on the budget
# - It use a smarter heuristic than the provided
# --------------------------------------------------------
import math
import random
import time
import numpy as np

from Game.Action import Action
from Game.ForwardModel import ForwardModel
from Players.MyHeuristic import MyHeuristic
from Players.Player import Player


# ---------------------------------------------------------------------------
# N-times Turn Looking Ahead
# ---------------------------------------------------------------------------
class Bot3(Player):
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = MyHeuristic()           # My own heuristic

    def think(self, observation, budget):
        t0 = time.time()
        list_actions = observation.get_list_actions()

        if len(list_actions) == 1:
            return list_actions[0]

        player_id = observation.turn                           # id of the actual player
        l_acm = [0]*observation.hands[observation.turn].len()  # acumulated value for each action

        if observation.playing_cards.len() == 3:  # if the player is the last in the round, it has no sense to repeat
            self.test_actions(observation, list_actions, player_id, l_acm)
        else:
            i = 0
            while time.time() - t0 < budget - 0.1:
                self.test_actions(observation, list_actions, player_id, l_acm)    # test three actions
                i += 1

        idx = self.get_best_action(l_acm)
        return list_actions[idx]

    def test_actions(self, observation, list_actions, player_id, l_acm):
        rnd_obs = observation.get_randomized_clone()        # each time the observation change
        ath = 0
        for action in list_actions:
            num_played_cards = rnd_obs.playing_cards.len()  # how many players have already played
            new_obs = rnd_obs.clone()
            value = self.forward_model.play(new_obs, action, self.heuristic)  # play action
            num_played_cards += 1
            other_player_id = player_id + 1

            while num_played_cards < rnd_obs.n_players:  # finish the turn
                value, other_player_id, num_played_cards = self.play_other_player(num_played_cards, other_player_id,
                                                                                  new_obs)

            if rnd_obs.playing_cards.len() == 1 or rnd_obs.playing_cards.len() == 3:
                l_acm[ath] += value
            else:
                l_acm[ath] -= value
            ath += 1

    # Other players play random
    def play_other_player(self, num_played_cards, other_player_id, new_obs):
        if other_player_id == new_obs.n_players:
            other_player_id = 0

        ith = random.choice(range(new_obs.hands[other_player_id].len()))
        c = new_obs.hands[other_player_id].get_card(ith)
        a = Action(c)
        value = self.forward_model.play(new_obs, a, self.heuristic)
        return value, other_player_id + 1, num_played_cards+1

    def get_best_action(self, l_acm):
        return np.argmax(l_acm)

    def __str__(self):
        return "Bot3"
