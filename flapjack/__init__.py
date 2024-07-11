from deck import Deck
from player import Player, Dealer
from game import Game
import sys
from rich.console import Console

if __name__ == "__main__":
    try:
        console = Console()
        game = Game(console)
        deck = Deck()
        deck.shuffle()
        player = Player()
        dealer = Dealer()
        game.play(player, dealer, deck, console)
    except KeyboardInterrupt:
        sys.exit()
