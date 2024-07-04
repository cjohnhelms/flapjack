from deck import Deck
import time

BACKSIDE = 'backside'

class Person():
    def __init__(self):
        self.hand: list[tuple] = []
        self.flapjacks: int = 500
        self.current_bet: int = 0
        self.hidden: bool = False

    def deal(self, deck):
        self.hand.append(deck.draw())

    @property
    def value(self) -> int:
        aces: int = 0
        res = 0
        for card in self.hand:
            rank = card[0]
            if rank in ('J', 'Q', 'K'):
                res += 10
            elif rank == 'A':
                aces += 1
            else:
                res += int(rank)
        if res > 10:
            res += aces
        else:
            res += aces * 10
        return res

    def display_cards(self, cards):
        rows: list[str] = ['', '', '', '', '', '', '', '', '']

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

class Player(Person):
    def take_bet(self):
        while True:
            try:
                print(f'Flapjacks: {self.flapjacks}')
                bet: int = int(input("Bet: "))
                if bet <= self.flapjacks:
                    self.current_bet = bet
                    break
                else:
                    print('Not enough flapjacks!')
            except ValueError:
                print('Please enter a number')

    def take_move(self, deck: Deck):
        while True:
            if len(self.hand) == 2:
                choice: str = input("(H)it, (S)tay, or (D)ouble down? ")
            else:
                choice: str = input("(H)it or (S)tay? ")
            if choice.lower() not in ['h', 's', 'd', 'p']:
                print('Please select a valid option.')
            else:
                match choice:
                    case 'h':
                        self.deal(deck)
                        self.hidden = False
                        return choice
                    case 's':
                        self.hidden = False
                        return choice
                    case 'd':
                        if (self.value - self.current_bet) <= self.current_bet:
                            self.deal(deck)
                            self.hidden = True
                            return choice
                        else:
                            print('Not enough flapjacks.')

class Dealer(Person):
    def __init__(self):
        Person.__init__(self)
        self.hidden = True

    def hit(self, deck: Deck):
        print('Dealer hits...')
        time.sleep(1)
        self.deal(deck)
        self.value
