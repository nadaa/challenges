from string import ascii_lowercase
import sys
import re

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = hang_graphics()
#ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.word = word.lower()
        self.guess = []

    def add_placeholder(self):
        self.guess = [PLACEHOLDER for c in self.word if c in ASCII]

    def find_char(self, ch):
        ascii_word = [c for c in self.word if c in ASCII]
        return [i for i in range(len(ascii_word)) if ch.lower() == ascii_word[i]]

    def check_win(self):
        ascii_word = [c for c in self.word if c in ASCII]
        return ascii_word == self.guess

    def play(self):
        while True:
            try:
                char = input('enter a letter: ')
                pos = self.find_char(char)
                if len(pos) > 0:
                    for p in pos:
                        self.guess[p] = char.lower()
                    print(self.guess)
                    if self.check_win():
                        print("you win")
                        break
                else:
                    print(next(HANG_GRAPHICS))
            except StopIteration:
                print('You loose')
                break

            # or use functions ...


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print(word)

    # init / call program
    game = Hangman(word)
    game.add_placeholder()
    print(game.guess)
    game.play()
