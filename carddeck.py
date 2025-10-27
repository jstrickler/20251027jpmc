import random
from card import Card

class CardDeck():
    # class data
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # new list
        for suit in self.SUITS:   # self.X
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    # @cards.setter
    # def cards(self, value):
    #     pass

    def shuffle(self):  # instance method
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        return f"CardDeck:{len(self._cards)}"
    
    def __repr__(self):
        return "CardDeck()"

d1 = CardDeck()
d2 = CardDeck()
d1.shuffle()
print(d1.cards)
for _ in range(5):
    card = d1.draw()
    print(card)
print(d1)
print(repr(d1))