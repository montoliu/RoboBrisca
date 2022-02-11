from unittest import TestCase

from Game.Card import Card
from Game.Common import is_better_card


class TestIsBetterCard(TestCase):
    def test_is_better_card(self):
                                                                          # trump       # round
        self.assertEqual(True, is_better_card(Card("E", 1), Card("E", 2), Card("E", 1), Card("C", 1)))
        self.assertEqual(True, is_better_card(Card("E", 3), Card("E", 2), Card("E", 1), Card("C", 1)))
        self.assertEqual(False, is_better_card(Card("E", 6), Card("E", 3), Card("E", 1), Card("C", 1)))
        self.assertEqual(False, is_better_card(Card("E", 6), Card("E", 7), Card("E", 1), Card("C", 1)))
        self.assertEqual(True, is_better_card(Card("E", 7), Card("E", 6), Card("E", 1), Card("C", 1)))
        self.assertEqual(True, is_better_card(Card("E", 3), Card("E", 6), Card("E", 1), Card("C", 1)))

        self.assertEqual(True, is_better_card(Card("E", 2), Card("C", 1), Card("E", 1), Card("R", 1)))
        self.assertEqual(False, is_better_card(Card("C", 3), Card("E", 2), Card("E", 1), Card("C", 1)))

        self.assertEqual(True, is_better_card(Card("E", 4), Card("C", 1), Card("E", 1), Card("C", 1)))
        self.assertEqual(False, is_better_card(Card("C", 1), Card("E", 7), Card("E", 1), Card("C", 1)))

        self.assertEqual(True, is_better_card(Card("C", 7), Card("B", 1), Card("E", 1), Card("C", 1)))

        self.assertEqual(True, is_better_card(Card("O", 3), Card("O", 5), Card("E", 1), Card("C", 1)))
        self.assertEqual(False, is_better_card(Card("O", 5), Card("O", 6), Card("E", 1), Card("C", 1)))
