# -----------------------------------
# DRL model
# -----------------------------------
import math
import random
import time
import numpy as np
import torch
from matplotlib import pylab as plt

from Game.Action import Action
from Game.BriscaGame import BriscaGame
from Game.Card import Card
from Game.ForwardModel import ForwardModel
from Game.GameState import GameState
from Players.MyHeuristic import MyHeuristic


# -----------------------------------------------------
# Deep Reinforcement Learning Code
# -----------------------------------------------------
class DRLModel:
    def __init__(self):
        self.all_cards = self.create_all_cards()    # all cards in the game
        self.ht = MyHeuristic()                    # my own heuristic

        learning_rate = 1e-3
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # use GPU (if it exists)
        #print(self.device)

        l1 = 280   # Input feature vector
        l2 = 150   # L2
        l3 = 100   # L3
        l4 = 3    # The output has 3 dimensions

        self.model = torch.nn.Sequential(
            torch.nn.Linear(l1, l2),
            torch.nn.ReLU(),
            torch.nn.Linear(l2, l3),
            torch.nn.ReLU(),
            torch.nn.Linear(l3, l4)
        )

        self.model.to(self.device)
        self.loss_fn = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)

    # create all cards of the game
    def create_all_cards(self):
        all_cards = []
        l_types = ["O", "E", "C", "B"]
        l_numbers = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        for card_type in l_types:
            for number in l_numbers:
                all_cards.append(Card(card_type, number))
        return all_cards

    # Gets the feature vector from an observation/game state and reward
    # Returns a numpy array
    def obs2fv(self, obs):
        fv = self.getFv(obs)
        return np.array(fv) + np.random.rand(1, len(fv)) / 10   # add some error

    # get FV from observation/game state
    def getFv(self, obs):
        fv = []

        # player hand 3x40
        k = 0
        p = obs.turn
        for j in range(obs.hands[p].len()):
            v = []
            for card in self.all_cards:
                if card == obs.hands[p].get_card(j):
                    v.append(1)
                else:
                    v.append(0)
            fv.extend(v)
            k += 1
        while k < 3:
            fv.extend([0] * 40)
            k += 1

        # playing cards 3x40
        j = 0
        for i in range(obs.playing_cards.len()):
            v = []
            for card in self.all_cards:
                if card == obs.playing_cards.get_card(i):
                    v.append(1)
                else:
                    v.append(0)
            fv.extend(v)
            j += 1
        while j < 3:
            fv.extend([0] * 40)
            j += 1

        # trump card 1x40
        v = []
        for card in self.all_cards:
            if card == obs.trump_card:
                v.append(1)
            else:
                v.append(0)
        fv.extend(v)
        return fv

    # given and observation return the score as numpy of the three actions
    def estimate(self, obs):
        fv_ = self.obs2fv(obs)                    # get fv as np vector
        fv = torch.from_numpy(fv_).float()        # get fv as tensor
        qval = self.model(fv.to(self.device))     # call to NN to estimate. Return tensor
        qval_ = qval.cpu().data.numpy()           # get np vector
        return qval_

    def player_turn(self, gs, fm, ht):
        fv_ = self.obs2fv(gs)
        fv = torch.from_numpy(fv_).float()
        qval = self.model(fv.to(self.device))

        n_cards_on_hand = gs.hands[gs.turn].len()
        action_idx = np.random.randint(0, n_cards_on_hand)          # always random

        reward = self.play_action(gs, fm, ht, action_idx)

        Y = torch.Tensor([reward]).detach()
        X = qval.squeeze()[action_idx]

        loss = self.loss_fn(X.to(self.device), Y[0].to(self.device))
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()

    def play_action(self, gs, fm, ht, action_idx):
        action = Action(gs.hands[gs.turn].get_card(action_idx))
        reward = fm.play(gs, action, ht)
        return reward

    # train the model
    def train(self, n_episodes):
        gs = GameState()
        gm = BriscaGame()
        fm = ForwardModel()
        ht = MyHeuristic()

        time_acm = 0
        loss_acm = 0
        for i in range(n_episodes):
            gm.reset(gs, random.choice(range(4)))

            t0 = time.time()
            while not gs.is_terminal():
                loss = self.player_turn(gs, fm, ht)
                loss_acm += loss

            time_acm += time.time() - t0

            each = 1000
            if i > 0 and i % each == 0:
                print(str(i) + " " + str(loss_acm/each) + " " + str(time_acm))
                loss_acm = 0
                time_acm = 0

            if i > 0 and i % (each*100) == 0:
                # save temp model
                temp_filename = "Out/T" + str(i) + ".nn"
                self.save_to_disk(temp_filename)

    def save_to_disk(self, filename):
        torch.save(self.model, filename)

    def load_from_disk(self, filename):
        self.model = torch.load(filename, map_location=torch.device(self.device))
        self.model.eval()

    # Deep copy of the game state
    def gs_clone(self, gs):
        new_gs = GameState()
        new_gs.main_deck = gs.main_deck.clone()
        new_gs.hands = self.clone_list(gs.hands)
        new_gs.trump_card = gs.trump_card
        new_gs.won_cards = self.clone_list(gs.won_cards)
        new_gs.turn = gs.turn
        new_gs.n_players = gs.n_players
        new_gs.playing_cards = gs.playing_cards.clone()
        new_gs.winner = gs.winner
        return new_gs

    # deep copy of a list
    def clone_list(self, old_list):
        new_list = []
        for element in old_list:
            new_list.append(element.clone())
        return new_list

