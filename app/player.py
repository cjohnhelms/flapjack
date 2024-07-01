class Person():
    def __init__(self):
        self.hand: list(tuple) = []
        self.value = 0
        self.flapjacks = 500
        self.current_bet = 0

    def deal(self, deck):
        self.hand.append(deck.draw())

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

class Player(Person):
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

class Dealer(Person):
    def displayHand(self):
        self.displayCards([ BACKSIDE ] + self.hand[1:])
