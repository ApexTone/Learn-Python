import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self)

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        print("Create new deck")
        while len(self.cards) != 0:
            self.cards.pop()
        for s in ["Clubs", "Hearts", "Spades", "Diamonds"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for card in self.cards:
            card.show()

    def left(self):
        return len(self.cards)

    def shuffle(self):
        print("Shuffle the deck")
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        print("Card drawn")
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())

    def show_hand(self):
        print("Showing hand")
        for card in self.hand:
            card.show()

    def discard(self):
        if len(self.hand) >= 1:
            discarded = self.hand.pop()
            print("Discard {}".format(discarded))
            return discarded
        else:
            print("Hand is already empty!")


if __name__ == '__main__':
    c = Card("Clubs", 6)
    c.show()

    d = Deck()
    d.shuffle()
    d.show()
    print(d.left())

    john = Hand()
    john.draw(d)
    john.draw(d)
    john.show_hand()
    john.discard()
    john.show_hand()
