class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                 "Ten", "Jack", "Queen", "King"]
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def compared_to(self, other_card):
        if self.rank > other_card.rank:
            return self
        elif other_card.rank > self.rank:
            return other_card
        else:
            if self.suit > other_card.suit:
                return self
            else:
                return other_card

    def __str__(self):

        new_card = self.ranks[self.rank] + " of " + self.suits[self.suit]
        return new_card
