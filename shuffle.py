#!/usr/bin/python3
"""This module is responsible for getting and presenting
sequences of moves in order to shuffle a Rubik's cube."""

import sys
from move_class import Move

def recycle_if_similar(current_move, previous_move):
    """If current_move and previous_move are similar (can cancel out), it generates a new current_move. Returns current_move."""
    if previous_move and current_move.is_similar_to(previous_move):
        previous_move = current_move
        current_move = recycle_if_similar(Move(), current_move)
    return current_move

def shuffle(moves=32, spacing=4):
    """Prints a line containing random cube moves (defaults to 32 of them), with spaces after each 4."""
    previous_move = None
    print('\nGenerating {} random moves...'.format(moves))
    for i in range(moves):
        move = recycle_if_similar(Move(), previous_move)
        previous_move = move
        print(move.cube_notation, end = ' ')
        if spacing and (i % spacing) == (spacing - 1):
            print('\t', end = '')

    print('') # Trailing blank line.

if __name__ == '__main__':
    MOVES = 32
    SPACE_FREQUENCY = 4
    if len(sys.argv) > 1:
        try:
            MOVES = sys.argv[1]
            MOVES = abs(int(MOVES))
        except:
            print('Usage: $./shuffle.py [amount of shuffle moves] [frequency of spacing]')
            exit()
        if len(sys.argv) > 2:
            SPACE_FREQUENCY = abs(int(sys.argv[2]))
    shuffle(MOVES, SPACE_FREQUENCY)
