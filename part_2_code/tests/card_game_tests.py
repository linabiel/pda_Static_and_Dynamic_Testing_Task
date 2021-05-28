from typing import Sequence
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("ace", 1)
        self.card2 = Card("clubs", 9)

        self.cards = [self.card1, self.card2]

    def test_can_check_for_ace(self):
        check_if_is_ace = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, check_if_is_ace)

    def test_highest_card(self):
        check_highest_card = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2.value, check_highest_card.value)

    def test_cards_total(self):
        cards_total = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 10", cards_total)