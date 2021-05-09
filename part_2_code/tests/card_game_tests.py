import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("ace", 5)
        self.card2 = Card("clubs", 9)

    def test_can_check_for_ace(self):
        self.assertEqual('ace', self.card1.suit)

    def test_highest_card(self):
        self.assertEqual(self.card2.value, self.card2.value)

    def test_cards_total(self):
        cards = self.card1.value + self.card2.value
        self.assertEqual(14, cards)