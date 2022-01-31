# --------------------------------------------------------
# - RoboBrisca
# - ForwardModel
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
from Game.Common import is_better_card, calculate_points


# ---------------------------------------------------------------------------
# Rules of the Brisca game
# ---------------------------------------------------------------------------
class ForwardModel:

    # Play an action given the actual state of the game.
    # Returns the reward obtained after playing the action
    def play(self, gs, action, ht):
        actual_player = gs.turn

        card = action.get_card()
        gs.hands[gs.turn].remove(card)   # Remove card from player hand
        gs.playing_cards.add_card(card)  # add to playing cards

        reward = ht.get_score(gs, actual_player)   # Estimate the reward.

        # if it is the fouth, check who is the winner of this round and move cards to won set
        if gs.playing_cards.len() == 4:
            winner = self.get_round_winner(gs.playing_cards, gs.trump_card, gs.turn)  # round winner
            gs.won_cards[winner].add_cards(gs.playing_cards.get_cards())              # cards to winner's won cards set
            gs.playing_cards.clear()
            gs.turn = winner

            # draw new cards starting by the winner
            if not gs.main_deck.empty():
                player_to_recieve_a_new_card = winner
                for i in range(gs.n_players):
                    new_card = gs.main_deck.draw()
                    gs.hands[player_to_recieve_a_new_card].add_card(new_card)
                    player_to_recieve_a_new_card += 1
                    if player_to_recieve_a_new_card == gs.n_players:
                        player_to_recieve_a_new_card = 0
        else:
            gs.turn = self.next_turn(gs.turn)

        return reward

    # Who plays next
    def next_turn(self, actual_turn):
        if actual_turn == 0:
            return 1
        elif actual_turn == 1:
            return 2
        elif actual_turn == 2:
            return 3
        elif actual_turn == 3:
            return 0

    # Who is the winner of the round
    def get_round_winner(self, playing_cards, trump_card, turn):
        winning_player = turn + 1
        if winning_player == 4:
            winning_player = 0
        best_card = playing_cards.get_card(0)

        p = winning_player
        for c in range(1, 4):
            p += 1
            if p == 4:
                p = 0

            card = playing_cards.get_card(c)

            if is_better_card(card, best_card, trump_card, playing_cards.get_card(0)):
                best_card = card
                winning_player = p

        return winning_player

    # Returns the number of points of the winner, if there is a winner.
    # This game is players 0 and 2 vs 1 and 3
    def check_winner(self, game_state):
        if not game_state.is_terminal():
            return -1                   # no winner yet

        # the winner is the player with more points
        p0_2 = calculate_points(game_state.won_cards[0].get_cards()) + calculate_points(game_state.won_cards[2].get_cards())
        p1_3 = calculate_points(game_state.won_cards[1].get_cards()) + calculate_points(game_state.won_cards[3].get_cards())

        if p0_2 > p1_3:
            game_state.winner = 0
        elif p0_2 < p1_3:
            game_state.winner = 1
        else:
            # if there is a tie, the team with more cards is the winner
            if game_state.won_cards[0].len() + game_state.won_cards[2].len() > \
                    game_state.won_cards[1].len() + game_state.won_cards[3].len():
                game_state.winner = 0
            else:
                game_state.winner = 1

    def get_points_player(self, player_id, game_state):
        return calculate_points(game_state.won_cards[player_id].get_cards())