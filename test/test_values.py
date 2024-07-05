import unittest
from src import player

class ValueTest(unittest.TestCase):

    def test_double_aces(self):
        subject = player.Player()
        subject.hand = [('A', 'HEARTS'), ('A', 'DIAMONDS')]
        self.assertEqual(subject.value, 12, 'Double aces are not calculated correctly.')

    def test_ace_bust(self):
        subject = player.Player()
        subject.hand = ([('A', 'HEARTS'), ('7', 'HEARTS'), ('4', 'DIAMONDS')])
        self.assertEqual(subject.value, 12, 'Ace is being counted high, casuing bust.')

    def test_aces_eight(self):
        subject = player.Player()
        subject.hand = ([('A', 'HEARTS'), ('A', 'DIAMONDS'), ('8', 'DIAMONDS')])
        self.assertEqual(subject.value, 20, 'Ace is being counted high, casuing bust.')

if __name__ == '__main__':
    unittest.main()
