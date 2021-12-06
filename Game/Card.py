# --------------------------------------------------------
# - RoboBrisca
# - Card
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------

# ---------------------------------------------------------------------------
# Card. It has a number and a type.
# get_value() returns the value of the card since, in this game, the value is not its number
# ---------------------------------------------------------------------------
class Card:
    def __init__(self, card_type, card_number):
        self.card_type = card_type      # "O", "E", "C", "B"
        self.card_number = card_number  # 1 to 7 and 10 to 12 (no 8 and 9)

    def get_type(self):
        return self.card_type

    def get_number(self):
        return self.card_number

    def get_value(self):
        if self.card_number == 1:
            return 11
        if self.card_number == 3:
            return 10
        if self.card_number == 12:
            return 4
        if self.card_number == 11:
            return 3
        if self.card_number == 10:
            return 2
        return 0

    def clone(self):
        new_card = Card(self.card_type, self.card_number)
        return new_card

    def __str__(self):
        return self.card_type + str(self.card_number)

    def __eq__(self, other):
        return self.card_type == other.card_type and self.card_number == other.card_number
