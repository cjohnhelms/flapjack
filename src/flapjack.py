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

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def exit_msg():
    clear()
    print('Thanks for playing!')
    time.sleep(1)
    clear()
    sys.exit()

def draw_screen(player: Player, dealer: Dealer, deck: Deck, player_hidden: bool, dealer_hidden: bool):
    clear()
    if dealer_hidden:
        dealer.display_cards([ BACKSIDE ] + dealer.hand[1:])
    else:
        player.get_value()
        dealer.display_cards(dealer.hand)
    print()
    print('-' * 20)
    print()
    print(f'Flapjacks: {player.flapjacks}')
    print(f'Current bet: {player.current_bet}')
    if player_hidden:
        player.display_cards([ BACKSIDE ] + player.hand[1:])
    else:
        player.get_value()
        player.display_cards(player.hand)

def init_hand(player: Player, dealer: Dealer, deck: Deck):
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
    print(divider)
    print("Welcome to Flapjack! It's like blackjack, but you're betting with pancakes.\nYou are starting out with 500 flapjacks.")
    print(divider)
    deck = Deck()
    deck.shuffle()
    dealer = Dealer()
    player = Player()
    while True:
        init_hand(player, dealer, deck)
        if player.flapjacks > 1:
            player.take_bet()
        else:
            print('Sorry, you\'re all out of flapjacks.')
            sys.exit()
        while True:
            draw_screen(player, dealer, deck, player.hidden, True)
 
            player.get_value()
            if player.value > 21:
                break

            move: str = player.take_move(deck)
            match move:
                case 'h':
                    continue
                case 's':
                    break
                case 'd':
                    draw_screen(player, dealer, deck, player.hidden, True)
                    break

        player.get_value()
        dealer.get_value()
        if player.value <= 21:
            dealer.get_value()
            while dealer.value < 17:
                dealer.hit(deck)
                draw_screen(player, dealer, deck, player.hidden, True)

        time.sleep(1)
        draw_screen(player, dealer, deck, False, False)
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

        cont = input('Play again? (y/n) ').lower()
        while True:
            if cont not in ['y', 'n']:
                print("Please select yes or no.")
            else:
                if cont == 'y':
                    clear()
                    break
                else:
                    exit_msg()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit_msg()

