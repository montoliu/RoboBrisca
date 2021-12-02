# ---------------------------------------------------------------------------
# An Action is just the card to be played
# ---------------------------------------------------------------------------
class Action:
    def __init__(self, card):
        self.card = card

    def get_card(self):
        return self.card

    def __str__(self):
        return str(self.card)
