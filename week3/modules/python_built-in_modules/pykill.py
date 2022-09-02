# A python program to kill/force windows apps to stop
import os
import sys
import argparse

# pykill.py cmd1 cmd2 cmd3
# pykill.py -p command

def kill_process_by_name(process_name):
    """
    This function terminates a given process by its name
    :params process_name
    """
    # This command only works on windows
    command = f"taskkill /f /im {process_name}.exe"
    os.system(command)


def main():
    "Main driver of the program"
    parser = argparse.ArgumentParser(description="Kill process by name")
    parser.add_argument('-p', '--process_name' ,help="Enter process name to kill")
    args = parser.parse_args()

    if args.process_name:
        kill_process_by_name(args.process_name)
    else:
        parser.print_help()
        sys.exit(-1)


if __name__ == '__main__':
    main()

