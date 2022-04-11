# --------------------------------------------------------
# - RoboBrisca
# - Bot4 for first phase of Robobrisca competition
# - It is a Deep Reinforcement learning approach
# --------------------------------------------------------
import numpy as np
from Game.Action import Action
from Players.DRLModel import DRLModel
from Players.Player import Player


# --------------------------------
# DRL based Bot
# --------------------------------
class Bot4(Player):
    def __init__(self, filename):
        self.drlmodel = DRLModel()                # Creare empty drl model
        self.drlmodel.load_from_disk(filename)    # Load a previously trained NN
        self.filename = filename

    def think(self, observation, budget):
        # If there is just one card
        if observation.hands[observation.turn].len() == 1:
            return Action(observation.hands[observation.turn].get_card(0))

        est = self.drlmodel.estimate(observation)                             # return 1x3 np array
        idx = np.argmax(est[0, 0:observation.hands[observation.turn].len()])  # best
        return Action(observation.hands[observation.turn].get_card(idx))      # return selected action

        # t0 = time.time()
        # i = 0
        # acm = [0, 0, 0]
        # #while time.time()-t0 < budget - 0.1:
        # while i < 1000:
        #     new_obs = observation.get_randomized_clone()    # randomize observation
        #     est = self.drlmodel.estimate(new_obs)           # return 1x3 np array
        #     for j in range(3):
        #         acm[j] += est[0][j]
        #     i += 1
        #
        # # get best action
        # best_idx = 0
        # best_score = -math.inf
        # for i in range(observation.hands[observation.turn].len()):
        #     if acm[i] > best_score:
        #         best_score = acm[i]
        #         best_idx = i
        #
        # return Action(observation.hands[observation.turn].get_card(best_idx))  # return selected action

    def __str__(self):
        return "Bot4 [" + self.filename + "]"
