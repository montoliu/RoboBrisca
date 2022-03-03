# --------------------------------------------------------
# - RoboBrisca
# - BriscaGame
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
import random
from Game.Action import Action


# -----------------------------------------------------------
# A Game state view for a particular player
# The non observable parts have been randomized.
# -----------------------------------------------------------
from Game.CardCollection import CardCollection


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

    # Randomize
    def get_randomized_clone(self):
        l_all_cards = []
        l_all_cards.extend(self.main_deck.get_cards_less_last())  # last one is the trump one
        for p in range(self.n_players):
            if p != self.turn:
                l_all_cards.extend(self.hands[p].get_cards())

        random.shuffle(l_all_cards)

        # draw cards to opponent hand
        randomized_main_deck = CardCollection()
        randomized_main_deck.add_cards(l_all_cards)
        randomized_hands = []

        for p in range(self.n_players):
            randomized_hands.append(CardCollection())
            n = self.hands[p].len()  # number of card on hand
            if p != self.turn:
                # draw n cards from randomized main_deck. n is the same number of card that the player has on hand
                for i in range(n):
                    card = randomized_main_deck.draw()
                    randomized_hands[p].add_card(card)
            else:
                # same cards for actual player
                for i in range(n):
                    card = self.hands[p].get_card(i)
                    randomized_hands[p].add_card(card)

        # add trump card
        if not self.main_deck.empty():
            randomized_main_deck.add_card(self.trump_card)

        obs = Observation(randomized_main_deck, randomized_hands, self.trump_card,
                          self.won_cards, self.turn, self.n_players, self.playing_cards, self.winner)
        return obs
