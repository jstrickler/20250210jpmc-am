class Card:  # inherits from 'object'
    def __init__(self, rank, suit):        
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):  # getter property
        return self._rank

    # rank = property(rank)

    @property
    def suit(self):
        return self._suit
    
    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('6', 'Clubs')
    print(c1)   # str(c1)
    # c1.get_rank()
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    print(repr(c1))
    print(f"{c1 = }")
    c2 = Card('J', 'Diamonds')
    print(f"{c2 = }")
    print(c2)
    cards = [c1, c2]
    print(cards)