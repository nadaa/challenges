from pyfiglet import figlet_format
from termcolor import *
import colorama
from datetime import time
from time import sleep
import sys


def print_logo():
    colorama.init()
    print()
    cprint(figlet_format('Pomodoro App', font='slant'), 'green')


def pomodoro():
    period = int(input("Enter the period in minutes: "))
    min = period -1
    sec = 59
    t = time(0, min, sec, 0)
    while t.second > 0:
        sys.stdout.write(str(t)+'\r')
        sys.stdout.flush()
        sleep(1)
        if sec > 0:
            sec -= 1
            t = time(0, min, sec, 0)
        else:
            if(t.minute>=1):
                sec = 59
                min = min - 1
                t = time(0, min, sec, 0)
    print(str(t))
    print('Beeb')

def main():
    print_logo()
    pomodoro()


if __name__ == '__main__':
    main()