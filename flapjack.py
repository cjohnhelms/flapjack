#!/usr/bin/env/pythn
import random
import time
import sys
from os import system, name

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
TITLE = """
                                                                                                    
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

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Player():
    def __init__(self):
        self.hand: list(tuple) = []
        self.value = 0
        self.flapjacks = 500
        self.current_bet = 0

    def deal(self, deck):
        self.hand.append(deck.draw())

    def takeBet(self):
        while True:
            try:
                print(f'Flapjacks: {self.flapjacks}')
                bet = int(input("Bet: "))
                if bet <= self.flapjacks:
                    self.current_bet = bet
                    break
                else:
                    print('Not enough flapjacks!')
            except ValueError:
                print('Please enter a number')

    def takeMove(self):
        while True:
            choice = input("(H)it or (S)tay? ")
            if choice.lower() not in ['h', 's']:
                print('Please select hit or stay.')
            else:
                return choice

    def getValue(self):
        aces = 0
        self.value = 0
        for card in self.hand:
            rank = card[0]
            if rank in ('J', 'Q', 'K'):
                self.value += 10
            elif rank == 'A':
                aces += 1
            else:
                self.value += int(rank)
        if self.value > 10:
            self.value += aces
        else:
            self.value += aces * 10
    
    def displayCards(self, cards: list[tuple]):
        rows = ['', '', '', '', '', '', '', '', '']

        for i, card in enumerate(cards):
            rows[0] += ' _______  '
            if card == BACKSIDE:
                rows[1] += '|##     | '
                rows[2] += '|       | '
                rows[3] += '|       | '
                rows[4] += '|  ###  | '
                rows[5] += '|       | '
                rows[6] += '|       | '
                rows[7] += '|_____##| '
            else:
                rank, suit = card
                rows[1] += '|{}     | '.format(rank.ljust(2))
                rows[2] += '|       | '
                rows[3] += '|       | '
                rows[4] += '|   {}   | '.format(suit)
                rows[5] += '|       | '
                rows[6] += '|       | '
                rows[7] += '|_____{}| '.format(rank.rjust(2, '_'))
        for row in rows:
            print(row)

    def showHand(self):
        self.displayCards(self.hand)

class Dealer(Player):
    def displayHand(self):
        self.displayCards([ BACKSIDE ] + self.hand[1:])

class Deck:
    def __init__(self) -> list[tuple]:
        self.suits: list = [HEARTS, DIAMONDS, SPADES, CLUBS]
        self.ranks: list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards: list[tuple] = [ (rank, suit) for suit in self.suits for rank in self.ranks ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

def drawScreen(player: Player, dealer: Dealer, deck: Deck, reveal: bool):
    clear()
    if reveal:
        dealer.showHand()
        print(f'Total: {dealer.value}')
    else:
        dealer.displayHand()
    print()
    print('-' * 20)
    print()
    if reveal:
        print(f'Total: {player.value}')
    print(f'Flapjacks: {player.flapjacks}')
    print(f'Current bet: {player.current_bet}')
    player.showHand()

def initHand(player: Player, dealer: Dealer, deck: Deck):
    player.hand = []
    dealer.hand = []
    player.value = 0
    dealer.value = 0
    player.current_bet = 0
    player.deal(deck)
    dealer.deal(deck)
    player.deal(deck)
    dealer.deal(deck)

def main():
    clear()
    print(TITLE)
    print("-" * 30)
    print("Welcome to Flapjack! It's like blackjack, but you're betting with pancakes.\nYou are starting out with 500 flapjacks.")
    print("-" * 30)
    print()
    deck = Deck()
    deck.shuffle()
    dealer = Dealer()
    player = Player()
    while True:
        initHand(player, dealer, deck)
        if player.flapjacks > 1:
            player.takeBet()
        else:
            print('Sorry, you\'re all out of flapjacks.')
            sys.exit()
        while True:
            drawScreen(player, dealer, deck, False)
            
            player.getValue()
            if player.value > 21:
                print('Bust')
                break

            move = player.takeMove().upper()
            if move == 'D':
                player.current_bet += player.current_bet

            if move in ('H', 'D'):
                player.deal(deck)

            if move in ('S', 'D'):
                break

        player.getValue()
        if player.value <= 21:
            dealer.getValue()
            while dealer.value < 17:
                print('Dealer hits...')
                time.sleep(2)
                dealer.deal(deck)
                drawScreen(player, dealer, deck, False)

                dealer.getValue()
                if dealer.value > 21:
                    input('Press Enter to conitue...')
                    print()
        
        drawScreen(player, dealer, deck, True)
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

        cont = input('Play again? (y/n) ').lower()
        if cont == 'y':
            clear()
            continue
        else:
            print('Thanks for playing!')
            break
        
if __name__ == '__main__':
    main()

