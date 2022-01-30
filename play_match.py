# --------------------------------------------------------
# - RoboBrisca
# - play_match main program: play a game between two bots
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
import random

from Game.ForwardModel import ForwardModel
from Game.GameState import GameState
from Game.Heuristic import Heuristic
from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.HumanPlayer import HumanPlayer
from Players.OSLAPlayer import OSLAPlayer
from Players.SlowPlayer import SlowPlayer
from Players.RandomPlayer import RandomPlayer
from Game.BriscaGame import BriscaGame


# ---------------------------------------------------------------------------
# Play just one game between two players
# When the game ends, game_state.winner has the player id of the winner (0 or 1)
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 1                  # Time to think for AI in second
    verbose = True              # print messages ON/OFF
    controlling_time = True    # If the player time to think is going to be controlled (True/False)
    save_game = True            # If the game is saved to be studied in the future (True/False)
    save_name = "Out/game.txt"  # Filename when the game is going to be saved

    # Main objects for Brisca Game
    game = BriscaGame()                  # Game class
    game_state = GameState()             # Game state of the game
    heuristic = Heuristic()              # Heuristic to known how good is to be in a particular game state
    forward_model = ForwardModel()       # Rules of the game

    player_id_as_first = random.choice(range(game_state.n_players))        # who starts is determined randomly
    game.reset(game_state, player_id_as_first)                             # Game initialization

    l_players = [RandomPlayer(), OSLAPlayer()]    # list of Players

    if save_game:
        game.save_game_on(save_name)

    game.run(game_state, forward_model, heuristic, l_players, budget, verbose, controlling_time)  # run the game

    if verbose:
        print("")
        print("*** ------------------------------------------------- ")
        if game_state.winner != -1:
            print("*** The winner is the player: " + str(game_state.winner) + " " + str(l_players[game_state.winner]))
        else:
            print("*** There is a Tie.")
        print("*** ------------------------------------------------- ")
