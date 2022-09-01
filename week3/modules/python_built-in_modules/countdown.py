# create a countdown timer
import time
import datetime
import sys

def countdown_timer():
    if len(sys.argv) == 2:
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            print("Please enter a valid number")
            sys.exit(1)
    else:
        print("Please enter a valid number")
        sys.exit(1)
    while countdown > 0:
        # format the countdown timer: 00:00:00
        # t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3].replace(" ", "T")
        # format the countdown timeer in the format: 00:00:00
        countdown_time = str(datetime.timedelta(seconds=countdown))
        # print the countdown timer
        print(countdown_time)
        time.sleep(1)
        countdown -= 1
    print("Countdown finished")

def main():
    usage = "Usage: countdown.py <number>"
    if len(sys.argv) == 2:
        countdown_timer()
    else:
        print(usage)

if __name__ == '__main__':
    main()