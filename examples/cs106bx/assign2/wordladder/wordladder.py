#!/usr/bin/env python
"""CS106B/X Assignment 2 Example: Word Ladder


"""
from campy.datastructures.lexicon import Lexicon
from campy.util.simpio import get_line


def greet():
    print("Welcome to CS 106B/X Word Ladder!")
    print("Please give me two English words, and I will convert the")
    print("first into the second by modifying one letter at a time.")
    print()

def load_dictionary():
    # TODO(sredmond): Handle bad dictionary name.
    return Lexicon(get_line("Dictionary file name:"))

if __name__ == '__main__':
    greet()
    # TODO(sredmond): Finish wordladder!
