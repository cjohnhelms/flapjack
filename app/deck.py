class Deck:
    def __init__(self) -> list[tuple]:
        self.suits: list = [HEARTS, DIAMONDS, SPADES, CLUBS]
        self.ranks: list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards: list[tuple] = [ (rank, suit) for suit in self.suits for rank in self.ranks ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
