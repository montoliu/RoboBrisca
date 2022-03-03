# --------------------------------------------------------
# - RoboBrisca
# - CardCollection
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
import random


# ---------------------------------------------------------------------------
# A list of cards
# It can be used as Deck, hand, etc.
# ---------------------------------------------------------------------------
class CardCollection:
    def __init__(self):
        self.l_cards = []

    def clear(self):
        self.l_cards.clear()

    def add_card(self, card):
        self.l_cards.append(card)

    def add_cards(self, l_cards):
        self.l_cards.extend(l_cards)

    def shuffle(self):
        random.shuffle(self.l_cards)

    def get_last_card(self):
        return self.l_cards[len(self.l_cards)-1]

    def len(self):
        return len(self.l_cards)

    def draw(self):
        card = self.l_cards[0]
        self.l_cards.pop(0)
        return card

    def get_cards(self):
        return self.l_cards

    def get_cards_less_last(self):
        return self.l_cards[:len(self.l_cards)-1]

    def get_card(self, ith):
        return self.l_cards[ith]

    # Deep copy
    def clone(self):
        new_card_collection = CardCollection()
        new_card_collection.l_cards = []

        for card in self.l_cards:
            new_card = card.clone()
            new_card_collection.add_card(new_card)

        return new_card_collection

    def empty(self):
        if self.l_cards:
            return False
        return True

    def remove(self, card):
        self.l_cards.remove(card)

    def __str__(self):
        s = ""
        for card in self.l_cards:
            s += str(card) + " "
        return s
