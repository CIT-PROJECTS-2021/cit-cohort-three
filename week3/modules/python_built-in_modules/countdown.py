# Import required modules
import sys
import time
import datetime


# function to show usage of our program
def usage():
    print("countdown.py <number>")

# coutdown timer function
def countdown_timer():
    print(sys.argv)
    # check if the user passed in any commandline arguments
    if len(sys.argv) == 2:
        # check if argument can be converted to an int
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            # Throw an error because argument is not integer convertible
            print("Please enter a valid number")
            sys.exit(-1)
    else:
        # show usage if no arguments passed or if more that required passed
        usage()
        sys.exit(-1)
    
    # create an infinite loop
    while countdown > 0:
        # 00:00:00
        # create time and convert it to string using timedelta function
        # from datetime
        countdown_time = str(datetime.timedelta(seconds=countdown))

        # print time
        print(countdown_time)
        # wait for one second
        time.sleep(1)
        # decrement countdown seconds by 1
        countdown -= 1
    # print finished when the loop ends
    print("countdown finished")


# create main function
def main():
    countdown_timer()


# invoke main function
if __name__ == '__main__':
    main()
