from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY) as f:
        words = f.readlines()
    return [word.strip() for word in words]


def calc_word_value(w):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[l.upper()] for l in w if l != '-'])


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return sorted(words, key=lambda w: calc_word_value(w), reverse=True)[0]


if __name__ == "__main__":
    pass  # run unittests to validate
