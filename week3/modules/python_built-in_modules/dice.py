# Dice game in Python

import random

def roll_dice():
    """Rolls a dice and returns the result"""
    return random.randint(1, 6)

def is_valid_input(user_input):
    """Checks if the user input is valid"""
    if user_input == "r" or user_input == "R":
        return True
    elif user_input == "q" or user_input == "Q":
        return True
    else:
        return False

def is_winner(user_score, computer_score):
    """Checks if the user or the computer has won"""
    if user_score >= 100:
        return True
    elif computer_score >= 100:
        return True
    else:
        return False


def is_six(user_input):
    """Checks if the user rolled a six"""
    if user_input == 6:
        return True
    else:
        return False

def main():
    """Main function"""
    user_score = 0
    computer_score = 0
    while True:
        user_input = input("Press r to roll the dice and q to quit: ")
        if is_valid_input(user_input):
            if user_input == "r" or user_input == "R":
                user_input = roll_dice()
                if is_six(user_input):
                    user_score += 10
                else:
                    user_score += user_input
                print("You rolled a " + str(user_input))
                print("Your score is " + str(user_score))
                computer_input = roll_dice()
                if is_six(computer_input):
                    computer_score += 10
                else:
                    computer_score += computer_input
                print("The computer rolled a " + str(computer_input))
                print("The computer score is " + str(computer_score))
                if is_winner(user_score, computer_score):
                    if user_score > computer_score:
                        print("You won!")
                    else:
                        print("The computer won!")
                    break
            elif user_input == "q" or user_input == "Q":
                break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()