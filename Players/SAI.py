# 4st position on first edition

import math
import random
import time

from Game.Action import Action
from Game.ForwardModel import ForwardModel
from Game.Heuristic import Heuristic
from Players.Player import Player


class SAIPlayer(Player):
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = Heuristic()

    def think(self, observation, budget):
        time_start = 0
        time_end = 0
        time_general = 0
        budget_range = 1
        i = 0
        count = True
        list_actions = observation.get_list_actions()
        player_id = observation.turn
        pos = observation.playing_cards.len()
        pos_initial = pos
        turn_heuristic = []
        final_heuristic = []
        best_score = -math.inf
        best_action = 0

        while i < budget_range:
            for action in list_actions:
                if count:
                    time_start = time.perf_counter()
                new_obs = observation.get_randomized_clone()
                score = self.forward_model.play(new_obs, action, self.heuristic)
                turn_heuristic.append(score)
                pos += 1
                other_player = player_id + 1

                while pos < 4:

                    if other_player == 4:
                        other_player = 0

                    other_card = new_obs.hands[other_player].get_card(random.choice(range(new_obs.hands[other_player].len())))          # Selecciona una carta al azar de otro jugador
                    other_action = Action(other_card)                                                   # Transfoma la carta elegida a una acción
                    other_score = self.forward_model.play(new_obs, other_action, self.heuristic)        # Juega la carta del otro jugador
                    turn_heuristic.append(other_score)
                    pos += 1
                    other_player += 1

                if pos_initial == 0:
                    team1 = turn_heuristic[0] + turn_heuristic[2]
                    team2 = turn_heuristic[1] + turn_heuristic[3]

                elif pos_initial == 1:
                    team1 = turn_heuristic[0] + turn_heuristic[2]
                    team2 = turn_heuristic[1]

                elif pos_initial == 2:
                    team1 = turn_heuristic[0]
                    team2 = turn_heuristic[1]

                else:
                    team1 = turn_heuristic[0]
                    team2 = 0

                heuristic_difference = team1 - team2
                final_heuristic.append(heuristic_difference)
                turn_heuristic = []
                pos = pos_initial

                if heuristic_difference > best_score:
                    best_score = heuristic_difference
                    best_action = action

            if count:
                time_end = time.perf_counter()
                time_general = time_end - time_start
                budget_range = (budget // time_general) - 500

            i += 1
            
        return best_action

    def __str__(self):
        return "SAI"
