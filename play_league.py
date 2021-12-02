from Game.ForwardModel import ForwardModel
from Game.BriscaGame import BriscaGame
from Game.GameState import GameState
from Game.Heuristic import Heuristic
from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.RandomPlayer import RandomPlayer


def actualize_points(l_pts, winner, ith, jth):
    if winner == 0:
        l_pts[ith] += 1
    elif winner == 1:
        l_pts[jth] += 1
    else:
        l_pts[ith] += 0.5  # When there is a Tie, half for each player
        l_pts[jth] += 0.5


def print_information(n_matches, l_players):
    print("This a tournament of game Brisca between players: ")
    i = 0
    for p in l_players:
        print(str(i) + " -> " + str(p))
        i += 1
    print("Number of games between two players: " + str(n_matches) + "\n")


# ---------------------------------------------------------------------------
# MAIN: Plays several games among several players
# The winning player of a game gets 1 point
# When there is a Tie, both players get 0.5 points
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 2                      # In second
    verbose = False                 # print messages OFF
    n_matches = 10
    controlling_time = False

    game = BriscaGame()
    game_state = GameState()
    heuristic = Heuristic()
    forward_model = ForwardModel()

    # List of players of the league
    l_players = [AlwaysFirstPlayer(), RandomPlayer(), RandomPlayer()]

    print_information(n_matches, l_players)

    l_points = [0.0 for i in range(len(l_players))]  # 0.0 points for each player
    n_matches = int(n_matches / 2)

    for i in range(len(l_players)):
        p1 = l_players[i]
        for j in range(i+1, len(l_players)):
            p2 = l_players[j]
            players = [p1, p2, p1, p2]

            for n in range(n_matches):
                # player i as first
                game.reset(game_state, 0)
                game.run(game_state, forward_model, heuristic, players, budget, verbose, controlling_time)
                actualize_points(l_points, game_state.winner, i, j)

                # player j as first
                game.reset(game_state, 1)
                game.run(game_state, forward_model, heuristic, players, budget, verbose,controlling_time)
                actualize_points(l_points, game_state.winner, i, j)

    for i in range(len(l_players)):
        print("Player " + str(i) + " -> " + str(l_players[i]) + " got " + str(l_points[i]) + " points")


