# -------------------------------------------------------------------
# - RoboBrisca
# - play_league main program: play a competition among several bots
# - Implemented by: Raul Montoliu (Dic 2021)
# -------------------------------------------------------------------
from time import sleep

from Game.ForwardModel import ForwardModel
from Game.BriscaGame import BriscaGame
from Game.GameState import GameState
from Game.Heuristic import Heuristic
from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.Bot1 import Bot1
from Players.Bot2 import Bot2
from Players.Bot3 import Bot3
from Players.Bot4 import Bot4
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer


def actualize_points(l_pts, winner, ith, jth):
    if winner == 0:
        l_pts[ith] += 1
    else:
        l_pts[jth] += 1


def print_information(n_matches, l_players):
    print("This a tournament of game Brisca between players: ")
    i = 0
    for p in l_players:
        print(str(i) + " -> " + str(p))
        i += 1
    print("Number of games between two players: " + str(n_matches) + "\n")


def print_winner(n, winner, p1, p2, l_points):
    if winner == 0:
        print(str(n) + " -> " + str(p1) + " : " + str(l_points))
    else:
        print(str(n) + " -> " + str(p2) + " : " + str(l_points))


# ---------------------------------------------------------------------------
# Plays several games among several players
# The winning player of a game gets 1 point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 1               # Time to think for AI in second
    verbose = False          # print messages ON/OFF
    controlling_time = True  # If the player time to think is going to be controlled True/False
    save_game = False        # If the game is saved to be studied in the future True/False
    save_name = "Out/game"
    n_matches = 10          # Matches between two bots
    sleep_time = 0           # time to sleep between games, It's just to add excitement for public watching the games

    game = BriscaGame()             # Game class
    game_state = GameState()        # Game state of the game
    heuristic = Heuristic()         # Heuristic to known how good is to be in a particular game state
    forward_model = ForwardModel()  # Rules of the game

    l_players = [Bot4("NN/bot4_1e4.nn"), OSLAPlayer()]  # List of players of the competition
    print_information(n_matches, l_players)

    l_points = [0.0 for i in range(len(l_players))]   # 0.0 points for each player
    n_matches = int(n_matches / 2)

    for i in range(len(l_players)):
        p1 = l_players[i]
        for j in range(i+1, len(l_players)):
            p2 = l_players[j]
            players = [p1, p2]          # Brisca is a game for 4 players

            # player ith vs jth
            print("-----------------------------------")
            print(str(p1) + " vs " + str(p2))
            print("-----------------------------------")
            for n in range(n_matches):
                # player i as first
                sleep(sleep_time)
                game.reset(game_state, 0)  # p1 plays as first
                if save_game:
                    fname = save_name + "_" + str(2*n) + ".txt"
                    game.save_game_on(fname)

                game.run(game_state, forward_model, heuristic, players, budget, verbose, controlling_time)
                actualize_points(l_points, game_state.winner, i, j)
                print_winner(2*n, game_state.winner, p1, p2, l_points)

                # player j as first
                sleep(sleep_time)
                game.reset(game_state, 1)  # p2 plays as first
                if save_game:
                    fname = save_name + "_" + str(2*n+1) + ".txt"
                    game.save_game_on(fname)

                game.run(game_state, forward_model, heuristic, players, budget, verbose,controlling_time)
                actualize_points(l_points, game_state.winner, i, j)
                print_winner(2*n+1, game_state.winner, p1, p2, l_points)

    # Show points
    print("-----------------------------------\n")
    for i in range(len(l_players)):
        print("Player " + str(i) + " -> " + str(l_players[i]) + " got " + str(l_points[i]) + " points")


