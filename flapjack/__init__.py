from deck import Deck
from player import Player, Dealer
from game import Game
import sys

if __name__ == "__main__":
    try:
        game = Game()
        deck = Deck()
        deck.shuffle()
        player = Player()
        dealer = Dealer()
        game.play(player, dealer, deck)
    except KeyboardInterrupt:
        sys.exit()
