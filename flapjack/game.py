#!/usr/bin/env/python

from player import Player, Dealer
from deck import Deck
import time
import sys
from os import system, name
from rich.table import Table

BACKSIDE: str = "backside"
TITLE: str = """

███████╗██╗      █████╗ ██████╗      ██╗ █████╗  ██████╗██╗  ██╗
██╔════╝██║     ██╔══██╗██╔══██╗     ██║██╔══██╗██╔════╝██║ ██╔╝
█████╗  ██║     ███████║██████╔╝     ██║███████║██║     █████╔╝
██╔══╝  ██║     ██╔══██║██╔═══╝ ██   ██║██╔══██║██║     ██╔═██╗
██║     ███████╗██║  ██║██║     ╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝      ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

"""


class Game:
    def clear(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def bye(self, console):
        self.clear()
        console.print("Thanks for playing!")
        time.sleep(1)
        self.clear()
        sys.exit()

    def __init__(self, console):
        self.clear()
        console.print(TITLE)
        console.print(
            "Welcome to Flapjack! It's like blackjack, but you're betting with pancakes.\nYou are starting out with 500 flapjacks.\n"
        )

    def draw_screen(
        self,
        player: Player,
        dealer: Dealer,
        deck: Deck,
        player_hidden,
        dealer_hidden,
        console,
    ):
        self.clear()
        dealer_table = Table()
        dealer_table.add_column("Rank", justify="left")
        dealer_table.add_column("Suit", justify="left")
        player_table = Table()
        player_table.add_column("Rank", justify="left")
        player_table.add_column("Suit", justify="left")

        if dealer_hidden:
            for card in [("X", "X")] + dealer.hand[1:]:
                dealer_table.add_row(card[0], card[1])
        else:
            for card in dealer.hand:
                dealer_table.add_row(card[0], card[1])
        if player_hidden:
            for card in [("X", "X")] + player.hand[:-1]:
                player_table.add_row(card[0], card[1])
        else:
            for card in player.hand:
                player_table.add_row(card[0], card[1])

        console.print()
        console.print(dealer_table)
        console.print("\n" + ("_" * 20) + "\n")
        console.print(player_table)

    def init_hand(self, player: Player, dealer: Dealer, deck: Deck):
        player.hand = []
        dealer.hand = []
        player.current_bet = 0
        player.hidden = False
        player.deal(deck)
        dealer.deal(deck)
        player.deal(deck)
        dealer.deal(deck)

    def check_flapjacks(self, player, console):
        if player.flapjacks > 1:
            player.take_bet()
        else:
            console.print("Sorry, you're all out of flapjacks.")
            sys.exit()

    def moves(self, player: Player, dealer: Dealer, deck: Deck, console):
        while True:
            self.draw_screen(player, dealer, deck, player.hidden, True, console)
            if player.value > 21:
                break
            move: str = player.take_move(deck)
            match move:
                case "h":
                    continue
                case "s":
                    break
                case "d":
                    self.draw_screen(player, dealer, deck, player.hidden, True, console)
                    break

    def calculate_scores(self, player: Player, dealer: Dealer, deck: Deck, console):
        if player.value <= 21:
            while dealer.value < 17:
                dealer.hit(deck)
                self.draw_screen(player, dealer, deck, player.hidden, True, console)
        input("Press any key to continue...")
        time.sleep(1)
        self.draw_screen(player, dealer, deck, False, False, console)
        console.print(f"Player total: {player.value}\tDealer total: {dealer.value}\n")
        if dealer.value > 21:
            console.print(f"Dealer busts, you won ${player.current_bet}!")
            player.flapjacks += player.current_bet
        elif (player.value > 21) or (player.value < dealer.value):
            console.print("You lose.")
            player.flapjacks -= player.current_bet
        elif player.value > dealer.value:
            console.print(f"You won ${player.current_bet}!")
            player.flapjacks += player.current_bet
        elif player.value == dealer.value:
            console.print("It's a tie, the bet is returned to you.")

    def play_again(self, console):
        cont = input("Play again? (y/n) ").lower()
        while True:
            if cont not in ["y", "n"]:
                console.print("Please select yes or no.")
            else:
                if cont == "y":
                    self.clear()
                    break
                else:
                    self.bye(console)

    def play(self, player, dealer, deck, console):
        while True:
            self.init_hand(player, dealer, deck)
            self.check_flapjacks(player, console)
            self.moves(player, dealer, deck, console)
            self.calculate_scores(player, dealer, deck, console)
            self.play_again(console)
