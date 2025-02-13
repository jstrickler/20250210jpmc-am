from card import Card
from carddeck import CardDeck

class GameMixin:
    pass

class JokerDeck(GameMixin, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for x in range(1, 3):
            card = Card(f"Joker{x}", "Joker")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    print(f"{j = }")
    print(f"{len(j) = }")
    j.shuffle()
    for i in range(3):
        print(j.draw())
    print(f"{j.cards = }")
