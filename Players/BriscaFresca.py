# 1st position on first edition

import random
import math
import time

from Game.BriscaGame import BriscaGame
from Game.CardCollection import CardCollection
from Game.Common import is_better_card, calculate_points
from Game.ForwardModel import ForwardModel
from Game.Heuristic import Heuristic
from Players.Player import Player


class Node:
    def __init__(self, parent, action, observation):
        self.parent = parent
        self.action = action
        self.l_children = []
        self.score = 0
        self.n = 0
        self.C = math.sqrt(2)
        self.BIG_NUMBER = 10E6
        self.observation = observation

    # --------------------------------------------
    # Return the child with best ucb1
    # --------------------------------------------
    def get_best_child(self):
        best_child = None
        best_ucb = -math.inf
        for child in self.l_children:
            epsilon = random.random() / 1000.0  # small number. It is used to have small differences in the ucb1
            if child.n == 0:  # not yet visited
                ucb_child = self.BIG_NUMBER + epsilon
            else:
                ucb_child = child.score + self.C * math.sqrt(math.log(self.n) / child.n) + epsilon
            if ucb_child >= best_ucb:
                best_child = child
                best_ucb = ucb_child

        return best_child

    def __str__(self):
        s = "Score: " + str(self.score) + " N: " + str(self.n) + " Action: " + str(self.action)
        return s


class RedefinedHeuristic:
    # Returns the points that the player_id is going to win in the actual round.
    # If the teammate is winning, returns +points.
    # If the player is going to lose, then returns -points.
    def get_score(self, observation, player_id):
        if observation.playing_cards.len() == 1:
            return observation.playing_cards.get_card(0).get_value()

        cards = observation.playing_cards.get_cards()
        points = 0
        for card in cards:
            points += card.get_value()

        if observation.playing_cards.len() == 2:
            player_card = observation.playing_cards.get_last_card()
            if not is_better_card(player_card, observation.playing_cards.get_card(0),
                                  observation.trump_card, observation.playing_cards.get_card(0)):
                return -points
        elif observation.playing_cards.len() == 3:
            if self.round_winner(observation.playing_cards, observation.trump_card) == 1:
                return -points
        elif observation.playing_cards.len() == 4:
            winner = self.round_winner(observation.playing_cards, observation.trump_card)
            if winner == 0 or winner == 2:
                return -points
        return points

    def round_winner(self, playing_cards, trump_card):
        best_card = playing_cards.get_card(0)

        winning_player = 0
        p = 0
        for c in range(1, playing_cards.len()):
            p += 1

            card = playing_cards.get_card(c)

            if is_better_card(card, best_card, trump_card, playing_cards.get_card(0)):
                best_card = card
                winning_player = p

        return winning_player


def is_terminal(new_obs):
    if calculate_points(new_obs.won_cards[0].get_cards()) + calculate_points(new_obs.won_cards[2].get_cards()) > 60:
        return True
    elif calculate_points(new_obs.won_cards[1].get_cards()) + calculate_points(new_obs.won_cards[3].get_cards()) > 60:
        return True
    else:
        return new_obs.main_deck.empty() \
               and new_obs.hands[0].empty() \
               and new_obs.hands[1].empty() \
               and new_obs.hands[2].empty() \
               and new_obs.hands[3].empty()


# Devuelve 0 si gana el primer bot y 1 si gana el segundo, -1 si hay empate técnico
def get_winner(new_obs, id):
    winner = 0
    p0_2 = calculate_points(new_obs.won_cards[0].get_cards()) + calculate_points(new_obs.won_cards[2].get_cards())
    p1_3 = calculate_points(new_obs.won_cards[1].get_cards()) + calculate_points(new_obs.won_cards[3].get_cards())

    # Si el id es 0, y gana p0_2, queremos que devuelva 1 (hemos ganado)
    # Si el id es 1, y gana p0_2, queremos que devuelva 0 (hemos perdido)
    # Si el id es 0, y gana p1_3, queremos que devuelva 0 (hemos perdido)
    # Si el id es 1, y gana p1_3, queremos que devuelva 1 (hemos ganado)

    if p0_2 > p1_3:
        return (1 + id) % 2
    elif p0_2 < p1_3:
        return (0 + id) % 2
    else:
        # if there is a tie, the team with more cards is the winner
        if new_obs.won_cards[0].len() + new_obs.won_cards[2].len() > \
                new_obs.won_cards[1].len() + new_obs.won_cards[3].len():
            return (1 + id) % 2
        else:
            return (0 + id) % 2


class BriscaFresca(Player):
    def __init__(self):
        self.count = 0
        self.n_nodes = 0
        self.id = -1
        self.forward_model = ForwardModel()
        self.heuristic = Heuristic()
        self.bgame = BriscaGame()
        self.deck = CardCollection()
        self.bgame.create_main_deck(self.deck)

    # --------------------------------------------
    # Return the best action to play
    # --------------------------------------------
    def think(self, observation, budget):
        start = time.time()
        # El id del jugador (0 o 1)
        self.id = observation.turn % 2
        self.count = 0
        self.n_nodes = 1
        root_node = Node(None, action=None, observation=observation)
        self.extend_node(root_node)
        self.rollout_one_random_child(root_node)

        i = 0
        while time.time() - start < budget - 0.1:
            # while i < 1000:
            child = root_node.get_best_child()  # Get the next child to be visited

            score = self.rollout(child)
            child.score = (child.score * child.n + score) / (child.n + 1)
            child.n += 1
            self.backpropagation(child.parent, score)

            i += 1

        # print("Iteraciones: " + str(i))
        recommend_child = self.recommend_child(root_node)
        return recommend_child.action

    # --------------------------------
    # Return the action corresponding to the best child of the root_node
    # --------------------------------
    def recommend_child(self, root_node):
        best_child = None
        best_score = -math.inf
        for child in root_node.l_children:
            if child.score >= best_score:
                best_score = child.score
                best_child = child
        return best_child

    # --------------------------------
    # Backpropagation
    # --------------------------------
    def backpropagation(self, node, score):
        while node is not None:
            node.score = (node.score * node.n + score) / (node.n + 1)
            node.n += 1
            node = node.parent

    # --------------------------------
    # Simulate the game until a non terminal node is reached
    # --------------------------------
    def rollout(self, node):
        new_obs = node.observation.clone()

        new_obs = new_obs.get_randomized_clone()

        while not is_terminal(new_obs):
            action = random.choice(new_obs.get_list_actions())
            self.forward_model.play(new_obs, action, self.heuristic)
            self.count += 1
        score = get_winner(new_obs, self.id)
        return score

    # --------------------------------
    # Randomly select one child to perform the rollout
    # --------------------------------
    def rollout_one_random_child(self, node):
        # Rollout just one random child
        one_child = random.choice(node.l_children)
        score = self.rollout(one_child)

        one_child.score = (one_child.score * one_child.n + score) / (one_child.n + 1)
        one_child.n += 1

        self.backpropagation(node, one_child.score)

    # --------------------------------
    # Extend node
    # Create a child for every possible action (only if the state changes).
    # Not add if the resulting state is the same as the parent. This is to prevent a->b->a
    # --------------------------------
    def extend_node(self, node):
        l_actions = node.observation.get_list_actions()

        for action in l_actions:
            new_observation = node.observation.clone()
            self.forward_model.play(new_observation, action, self.heuristic)
            self.count += 1
            node.l_children.append(Node(node, action, new_observation))

    def __str__(self):
        return "BriscaFresca"
