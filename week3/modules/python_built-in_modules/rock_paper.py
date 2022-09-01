# rock paper scissors game
# import required modules
import random

# create the playing function
def play():
    # get user input
    user = input("What is your choice? 'r' for rock, 'p' paper, 's' for scissors: ")
    
    # get computer choice
    computer = random.choice(['r', 'p', 's'])

    # check if user input is the same as computer choice
    if user == computer:
        return 'It is a tie!'

    #r>s, s>p, p>r
    # check if user selects r and computer selects s
    # or if user selects s and computer selects p
    # or if user selects p and computer selects r
    # if true, user wins otherwise computer wins
    if is_win(user, computer):
        return "You won!"

    return 'You Lost!'

def is_win(player, opponent):
    print(f"user: {player}")
    print(f"computer: {opponent}")
    # return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


# create main function
def main():
    print(play())


# invoke main function
if __name__ == "__main__":
    main()

# The importance of the __name__ == '__main__' statement
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do