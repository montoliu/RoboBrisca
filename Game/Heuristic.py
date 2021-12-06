# --------------------------------------------------------
# - RoboBrisca
# - BriscaGame
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
from Game.Common import is_better_card


class Heuristic:
    # Returns the points that the player_id is going to win in the acual round.
    # If the player is goinf to lose, then returns -points.
    def get_score(self, observation, player_id):
        if observation.playing_cards.len() == 1:
            return observation.playing_cards.get_card(0).get_value()

        cards = observation.playing_cards.get_cards()
        points = 0
        for card in cards:
            points += card.get_value()

        player_card = observation.playing_cards.get_last_card()
        is_better = True
        for i in range(observation.playing_cards.len() - 1):
            if not is_better_card(player_card, observation.playing_cards.get_card(i),
                                  observation.trump_card, observation.playing_cards.get_card(0)):
                is_better = False
                break

        if is_better:
            return points
        else:
            return -points
