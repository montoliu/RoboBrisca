# --------------------------------------------------------
# - RoboBrisca
# - Common
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------

# ---------------------------------------------------------------------------
# Some functions that can be used by several classes
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Returns True is actual_card is better than prev_card
# ---------------------------------------------------------------------------
def is_better_card(actual_card, prev_card, trump_card, round_card):
    # both cards are trump type
    if actual_card.get_type() == trump_card.get_type() and prev_card.get_type() == trump_card.get_type():
        if actual_card.get_value() > prev_card.get_value():
            return True
        elif actual_card.get_value() == prev_card.get_value(): # both 0 value e.g. E4 and E6
            return actual_card.card_number > prev_card.card_number
        else:
            return False
    elif actual_card.get_type() == trump_card.get_type():  # actual is trump, prev not
        return True
    elif prev_card.get_type() == trump_card.get_type():    # prev is trump, actual not
        return False

    # boths cards are round type
    if actual_card.get_type() == round_card.get_type() and prev_card.get_type() == round_card.get_type():
        if actual_card.get_value() > prev_card.get_value():
            return True
        elif actual_card.get_value() == prev_card.get_value():  # both 0 value e.g. E4 and E6
            return actual_card.card_number > prev_card.card_number
        else:
            return False
    elif actual_card.get_type() == round_card.get_type():  # actual is round, prev not
        return True
    elif prev_card.get_type() == round_card.get_type(): # prev is round, actual not
        return False

    if actual_card.get_value() > prev_card.get_value():
        return True
    elif actual_card.get_value() == prev_card.get_value():  # both 0 value e.g. E4 and E6
        return actual_card.card_number > prev_card.card_number

    return False


# ---------------------------------------------------------------------------
# Returns the sum of the points of all card in a list
# ---------------------------------------------------------------------------
def calculate_points(l_cards):
    points = 0
    for card in l_cards:
        points += card.get_value()
    return points
