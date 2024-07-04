#!/usr/bin/env/pythn

from player import Player, Dealer
from deck import Deck
import time
import sys
from os import system, name

BACKSIDE: str = 'backside'
divider: str = '\n' + ('-' * 20) + '\n'
TITLE: str = """

                          ████▓▓████████▓▓████▒▒████████▓▓▓▓▓▓██▓▓██
                    ██████░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒██████
              ██████░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████
          ▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓██▓▓
        ██░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓██
      ██░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓          ▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██
    ██░░▒▒░░▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓                ▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓██
    ██▒▒░░▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓                  ▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓██
  ██░░▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓              ████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓░░██
  ██▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░██
  ██▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓░░██
  ██▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓░░▒▒██
  ██░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░▒▒░░██
  ██░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▒▒▓▓▓▓░░░░▒▒░░░░██
  ░░▓▓░░░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒░░░░▓▓▓▓▓▓
    ██░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒▒▒░░░░░░░░██▓▓▓▓██
      ██░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░██▓▓▓▓▓▓▓▓██
        ██░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓██
          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓░░██
          ██░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░██
          ██░░▒▒▓▓▓▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓░░██
          ██▒▒░░▒▒▒▒▒▒▓▓▓▓██████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░▓▓██
          ██░░▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓░░▓▓░░██
          ██░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓░░░░▓▓░░░░██
            ██░░░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░░░░░▓▓▓▓░░░░██
            ██░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓░░░░░░░░████
              ██░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓░░░░░░░░░░░░██▓▓██
            ▓▓░░▓▓░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░▓▓
            ██░░▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓░░██
            ██░░▒▒▒▒▓▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████▓▓▓▓▓▓▓▓▓▓░░██
            ██▒▒░░▒▒▒▒▓▓▓▓▓▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓██
            ██░░▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓██████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓░░██
            ██░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓░░░░▓▓░░░░██
            ░░██░░░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓▒▒▓▓░░░░░░▓▓▓▓░░░░██░░
              ██░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓▓▓▓▓░░░░░░░░██
                ██░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓░░░░░░░░░░░░██
                  ██░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░██
                  ░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓
                        ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████
                        ░░░░░░▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░
                                    ██████████████████████████████████████████


███████╗██╗      █████╗ ██████╗      ██╗ █████╗  ██████╗██╗  ██╗
██╔════╝██║     ██╔══██╗██╔══██╗     ██║██╔══██╗██╔════╝██║ ██╔╝
█████╗  ██║     ███████║██████╔╝     ██║███████║██║     █████╔╝
██╔══╝  ██║     ██╔══██║██╔═══╝ ██   ██║██╔══██║██║     ██╔═██╗
██║     ███████╗██║  ██║██║     ╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝      ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

"""

def bye():
    clear()
    print('Thanks for playing!')
    time.sleep(1)
    clear()
    sys.exit()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Game:
    def __init__(self):
        clear()
        print(TITLE)
        print(divider)
        print("Welcome to Flapjack! It's like blackjack, but you're betting with pancakes.\nYou are starting out with 500 flapjacks.")
        print(divider)

    def draw_screen(self, player: Player, dealer: Dealer, deck: Deck, player_hidden: bool, dealer_hidden: bool):
        clear()
        if dealer_hidden:
            dealer.display_cards([ BACKSIDE ] + dealer.hand[1:])
        else:
            dealer.display_cards(dealer.hand)
        print()
        print('-' * 20)
        print()
        print(f'Flapjacks: {player.flapjacks}')
        print(f'Current bet: {player.current_bet}')
        if player_hidden:
            player.display_cards([ BACKSIDE ] + player.hand[1:])
        else:
            player.display_cards(player.hand)

    def init_hand(self, player: Player, dealer: Dealer, deck: Deck):
        player.hand = []
        dealer.hand = []
        player.current_bet = 0
        player.hidden = False
        player.deal(deck)
        dealer.deal(deck)
        player.deal(deck)
        dealer.deal(deck)

    def check_flapjacks(self, player):
        if player.flapjacks > 1:
            player.take_bet()
        else:
            print('Sorry, you\'re all out of flapjacks.')
            sys.exit()

    def moves(self, player: Player, dealer: Dealer, deck: Deck):
        while True:
            self.draw_screen(player, dealer, deck, player.hidden, True)
            if player.value > 21:
                break
            move: str = player.take_move(deck)
            match move:
                case 'h':
                    continue
                case 's':
                    break
                case 'd':
                    self.draw_screen(player, dealer, deck, player.hidden, True)

    def score(self, player: Player, dealer: Dealer, deck: Deck):
        time.sleep(1)
        self.draw_screen(player, dealer, deck, False, False)
        print(divider)
        print(f'Player total: {player.value}\tDealer total: {dealer.value}\n')
        if dealer.value > 21:
            print(f'Dealer busts, you won ${player.current_bet}!')
            player.flapjacks += player.current_bet
        elif (player.value > 21) or (player.value < dealer.value):
            print('You lose.')
            player.flapjacks -= player.current_bet
        elif player.value > dealer.value:
            print(f'You won ${player.current_bet}!')
            player.flapjacks += player.current_bet
        elif player.value == dealer.value:
            print('It\'s a tie, the bet is returned to you.')

    def play_again(self):
        cont = input('Play again? (y/n) ').lower()
        while True:
            if cont not in ['y', 'n']:
                print("Please select yes or no.")
            else:
                if cont == 'y':
                    clear()
                    break
                else:
                    bye()

    def play(self, player, dealer, deck):
        while True:
            self.init_hand(player, dealer, deck)
            self.check_flapjacks(player)
            self.moves(player, dealer, deck)
            self.score(player, dealer, deck)
            self.play_again()

if __name__ == '__main__':
    try:
        game = Game()
        deck = Deck()
        deck.shuffle()
        player = Player()
        dealer = Dealer()
        game.play(player, dealer, deck)
    except KeyboardInterrupt:
        bye()
