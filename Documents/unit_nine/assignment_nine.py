# Thenea Sun
# Nov. 29th
# This is a program about a game which designs a simplified game of Baccarat. The game is easy, but the program is hard.

import deck
import random


def main():
    while True:
        play = input("Do you want to start the game?(please enter 'y' or 'n')")
        if play == "y":
            deck1 = deck.Deck()
            deck1.shuffle()
            card1 = deck1.draw_a_card()
            card2 = deck1.draw_a_card()
            card3 = deck1.draw_a_card()
            card4 = deck1.draw_a_card()
            print("You got a", card1, "and a", card2)
            number1 = card1.get_rank() + 1 + card2.get_rank() + 1
            number2 = card3.get_rank() + 1 + card4.get_rank() + 1
            if number1 >= 10 and number1 < 20:
                number_x = number1 - 10
                print("Your number is", number_x)
            elif number1 >= 20:
                number_x = number1 - 20
                print("Your number is", number_x)
            else:
                number_x = number1
                print("Your number is", number_x)
            print("The dealer got a", card3, "and a", card4)
            if number2 >= 10 and number2 < 20:
                number_y = number2 - 10
                print("The dealer's number is", number_y)
            elif number2 >= 20:
                number_y = number2 - 20
                print("The dealer's number is", number_y)
            else:
                number_y = number2
                print("The dealer's number is", number_y)
            if number_x == 9 or number_x == 8 or number_y == 8 or number_y == 9:
                if number_x > number_y:
                    print("Nice! You win this one!")
                elif number_x == number_y:
                    print("This is a tie!")
                else:
                    print("I am sorry, The dealer wins this one")
            else:
                while True:
                    new_card = input("Would you like another card?(please enter'y' or 'n')")
                    if new_card == "y":
                        card5 = deck1.draw_a_card()
                        number3 = number_x + card5.rank + 1
                        if number3 >= 10 and number3 < 20:
                            number_z = number3 - 10
                            print("Your new number is", number_z)
                        elif number1 >= 20:
                            number_z = number3 - 20
                            print("Your new number is", number_z)
                        else:
                            number_z = number3
                            print("Your new number is", number_z)
                        if number_z == 9 or number_z == 8 or number_y == 8 or number_y == 9:
                            if number_z > number_y:
                                print("Nice! You win this one!")
                            elif number_z == number_y:
                                print("This is a tie!")
                            else:
                                print("I am sorry, The dealer wins this one")
                            break
                        else:
                            if number_z > number_y:
                                print("Nice! You win this one!")
                            elif number_z == number_y:
                                print("This is a tie!")
                            else:
                                print("I am sorry, The dealer wins this one")
                            break
                    elif new_card == "n":
                        if number_x > number_y:
                            print("Nice! You win this one!")
                        elif number_x == number_y:
                            print("This is a tie!")
                        else:
                            print("I am sorry, The dealer wins this one")
                        break
                    else:
                        print("Please follow the instruction")
                        pass
        elif play == "n":
            break
        else:
            print("please enter the right letter")
            pass


main()
