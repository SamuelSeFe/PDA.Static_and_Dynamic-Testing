import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Diamonds", 8)
        self.card3 = Card("Clubs", 5)
        self.cards = (self.card1, self.card2, self.card3)
    
    def test_check_for_ace_true(self):
        is_ace = self.game.check_for_ace(self.card1)
        self.assertEqual(True, is_ace)

    def test_check_for_ace_false(self):
        is_ace = self.game.check_for_ace(self.card2)
        self.assertEqual(False, is_ace)

    def test_check_highest_card1(self):
        high_card = self.game.highest_card(self.card2, self.card3)
        self.assertEqual(self.card2, high_card)
    
    def test_check_highest_card2(self):
        high_card = self.game.highest_card(self.card1, self.card3)
        self.assertEqual(self.card3, high_card)

    def test_total_cards(self):
        total = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 14", total)
