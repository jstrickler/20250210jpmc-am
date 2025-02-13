import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        return self._cards.pop()
    
    def __len__(self):
        return len(self._cards)

    # def __add__() 
    # def __eq__()

    def __str__(self):
        return f"CardDeck/{len(self)}"

    def __repr__(self):
        return "CardDeck()"

if __name__ == "__main__":
    d1 = CardDeck()
    print(f"{d1 = }")
    print(d1)
    d1.shuffle()
    print(f"{d1.cards = }")
    for i in range(5):
        print(d1.draw())
    print(f"{len(d1) = }")
    