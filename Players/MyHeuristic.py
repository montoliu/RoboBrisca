from Game.Common import is_better_card


class MyHeuristic:
    def get_score(self, observation, player_id):
        if observation.playing_cards.len() == 0:
            return 0

        # points of played cards
        cards = observation.playing_cards.get_cards()
        points = 0
        for card in cards:
            points += card.get_value()

        player_card = observation.playing_cards.get_last_card()
        first_card = observation.playing_cards.get_card(0)
        if observation.playing_cards.len() == 1:
            score = points
        elif observation.playing_cards.len() == 2:
            other_player_card = observation.playing_cards.get_card(0)
            if is_better_card(other_player_card, player_card, observation.trump_card, first_card):
                score = -points
            else:
                score = points
        elif observation.playing_cards.len() == 3:
            other_player_card = observation.playing_cards.get_card(1)
            my_mate_card = observation.playing_cards.get_card(0)
            if is_better_card(other_player_card, player_card, observation.trump_card, first_card) and \
                    is_better_card(other_player_card, my_mate_card, observation.trump_card, first_card):
                score = -points
            else:
                score = points
        else:
            other_player_card1 = observation.playing_cards.get_card(0)
            other_player_card2 = observation.playing_cards.get_card(2)
            my_mate_card = observation.playing_cards.get_card(1)
            if (is_better_card(other_player_card1, player_card, observation.trump_card, first_card) and
                    is_better_card(other_player_card1, my_mate_card, observation.trump_card, first_card)) or \
                (is_better_card(other_player_card2, player_card, observation.trump_card, first_card) and
                    is_better_card(other_player_card2, my_mate_card, observation.trump_card, first_card)):
                score = -points
            else:
                score = points

        return score
