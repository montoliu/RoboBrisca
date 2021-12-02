import random

from Game.ForwardModel import ForwardModel
from Game.GameState import GameState
from Game.Heuristic import Heuristic
from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.HumanPlayer import HumanPlayer
from Players.SlowPlayer import SlowPlayer
from Players.RandomPlayer import RandomPlayer
from Game.Game import Game


# ---------------------------------------------------------------------------
# MAIN: Play just one game between two players
# When the match ends, game_state.winner has the player id of the winner or -1 if there is a tie
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 2               # Time to think for AI in second
    verbose = True           # print messages ON/OFF
    controlling_time = True  # If the player time to think is going to be controlled ON/OFF
    # random.seed(1)         # random seed for debug

    game = Game()
    game_state = GameState()
    heuristic = Heuristic()
    forward_model = ForwardModel()

    player_id_as_first = random.choice(range(game_state.n_players))        # who starts
    game.reset(game_state, player_id_as_first)                             # Game initialization

    l_players = [RandomPlayer(), AlwaysFirstPlayer()]                      # Players

    game.run(game_state, forward_model, heuristic, l_players, budget, verbose, controlling_time)

    if verbose:
        print("")
        print("*** ------------------------------------------------- ")
        if game_state.winner != -1:
            print("*** The winner is the player: " + str(game_state.winner) + " " + str(l_players[game_state.winner]))
        else:
            print("*** There is a Tie.")
        print("*** ------------------------------------------------- ")

