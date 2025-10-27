class Card:
    # constructor (initializer)
    def __init__(self, rank, suit):
        # self._rank = rank
        # self.mango = rank
        self.rank = rank  # assign to property
        self.suit = suit
    
    @property
    def rank(self):  # getter property
        return self._rank
    
    @rank.setter
    def rank(self, value):  # setter property
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("suit must be a str")

    def __str__(self):
        return f"{self.rank}/{self.suit}"
# CardDeck DatabaseConnection  AccountID

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

c1 = Card('8', 'Diamonds')
print(c1)
print(c1.rank, c1.suit)
# c1.rank = 25
c2 = Card("10", "Clubs")
print(c2.rank, c2.suit)
print(repr(c1))