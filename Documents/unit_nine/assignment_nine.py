# Thenea Sun
# Nov. 29th
# This is a program about a game which designs a simplified game of Baccarat. The game is easy, but the program is hard.

import deck
import random


def main():
    deck1 = deck.Deck()
    deck1.shuffle()
    card1 = deck1.draw_a_card()
    card2 = deck1.draw_a_card()
    card3 = deck1.draw_a_card()
    card4 = deck1.draw_a_card()
    print("You got a", card1, "and a", card2)
    number1 = card1.rank + 1 + card2.rank + 1
    number2 = card3.rank + 1 + card4.rank + 1
    if number1 >= 10:
        number3 = number1 - 10
        print("Your number is", number3)
    else:
        print("Your number is", number1)
    print("The dealer got a", card3, "and a", card4)
    if number2 >= 10:
        number4 = number2 - 10
        print("The dealer's number is", number4)
    else:
        print("The dealer's number is", number2)
    if number2 == 9 or number2 == 8 or number1 == 8 or number1 == 9:
        if number1 > number2:
            print("Nice! You win this one!")
        elif number1 == number2:
            print("This is a tie!")
        else:
            print("I am sorry, The dealer wins this one")
    else:
        pass


main()
