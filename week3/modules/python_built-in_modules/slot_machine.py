# Python program for a slot machine

import random

# constants
NUM_REELS = 3
NUM_SYMBOLS = 7
NUM_SPINS = 10
MAX_BET = 10
MIN_BET = 1


def check_win(symbols):
    """Check if the symbols are the same"""
    return all(symbol == symbols[0] for symbol in symbols)


def get_symbols():
    """Get random symbols"""
    return [random.randint(1, NUM_SYMBOLS) for _ in range(NUM_REELS)]

def get_bet():
    """Get the bet"""
    bet = input("Enter bet: ")
    if bet.isdigit() and MIN_BET <= int(bet) <= MAX_BET:
        return int(bet)
    return 0

def main():
    """Main function"""
    bet = get_bet()
    if bet == 0:
        print("Invalid bet")
        return

    symbols = get_symbols()
    print(symbols)
    if check_win(symbols):
        print("You won ${}".format(bet * NUM_SYMBOLS))
    else:
        print("You lost ${}".format(bet))

if __name__ == "__main__":
    main()