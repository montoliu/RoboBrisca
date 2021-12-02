from Game.Action import Action


# -----------------------------------------------------------
# A Game state view for a particular player
# The non observable parts have been randomized.
# -----------------------------------------------------------
class Observation:
    def __init__(self, main_deck, hands, trump_card, won_cards, turn, n_players, playing_cards, winner):
        self.main_deck = main_deck.clone()
        self.hands = self.clone_list(hands)
        self.trump_card = trump_card
        self.won_cards = self.clone_list(won_cards)
        self.turn = turn
        self.n_players = n_players
        self.playing_cards = playing_cards.clone()
        self.winner = winner

    # Returns the actions that the player can play
    def get_list_actions(self):
        l_actions = []
        cards = self.hands[self.turn].get_cards()
        for card in cards:
            l_actions.append(Action(card))

        return l_actions

    # Deep copy
    def clone(self):
        new_main_deck = self.main_deck.clone()
        new_hands = self.clone_list(self.hands)
        new_trump_card = self.trump_card
        new_won_cards = self.clone_list(self.won_cards)
        new_turn = self.turn
        new_n_players = self.n_players
        new_playing_cards = self.playing_cards.clone()
        winner = self.winner
        new_obs = Observation(new_main_deck, new_hands, new_trump_card,
                              new_won_cards, new_turn, new_n_players, new_playing_cards, winner)
        return new_obs

    def clone_list(self, old_list):
        new_list = []
        for element in old_list:
            new_list.append(element.clone())
        return new_list
