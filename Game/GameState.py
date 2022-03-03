# --------------------------------------------------------
# - RoboBrisca
# - BriscaGame
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
import random
from Game.CardCollection import CardCollection
from Game.Observation import Observation


class GameState:
    def __init__(self):
        self.n_players = 4
        self.turn = 0
        self.trump_card = None
        self.playing_cards = CardCollection()
        self.main_deck = CardCollection()
        self.hands = []
        self.won_cards = []
        self.winner = -1

    # Get the observable view for actual player
    # non observable parts are randomized
    def get_observation(self):
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

    # Return True if the game state is terminl, i.e. when empty deck and empty hands
    def is_terminal(self):
        return self.main_deck.empty() \
               and self.hands[0].empty() \
               and self.hands[1].empty() \
               and self.hands[2].empty() \
               and self.hands[3].empty()

    def __str__(self):
        s = "DECK:  " + str(self.main_deck) + "\n"
        s += "TURN:  " + str(self.turn) + "\n"
        s += "TRUMP: " + str(self.trump_card) + "\n"
        s += "HANDS: \n"
        for hand in self.hands:
            s += "   " + str(hand) + "\n"
        s += "PLAYED CARDS: " + str(self.playing_cards) + "\n"
        s += "WON CARDS: \n"
        for cards in self.won_cards:
            s += "   " + str(cards) + "\n"
        return s
