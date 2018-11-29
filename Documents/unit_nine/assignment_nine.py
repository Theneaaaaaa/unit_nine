# Thenea Sun
# Nov. 29th
# This is a program about a game which designs a simplified game of Baccarat. The game is easy, but the program is hard.

import card
import random


class Deck:

    def __int__(self):

        self.deck_of_cards = []
        for rank in range(13):
            for suit in range(4):
                new_card = card.Card(rank, suit)
                self.deck_of_cards.append(new_card)

    def draw_a_card(self):
        new_card = self.deck_of_cards.pop()
        return new_card

    def shuffle(self):
        random.shuffle(self.deck_of_cards)


class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

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
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Right", "Nine", "Ten", "Jack", "Queen", "King"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        new_card = ranks[self.rank] + "of" + suits[self.suit]
        return new_card
