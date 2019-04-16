#!/usr/bin/python3

import random
import sys
from move import Move

def shuffle(moves = 32, spacing = 4):
  print('\nGenerating {} random moves...'.format(moves))
  for i in range(moves):
    move = Move()
    print(move.cubeNotation, end = ' ')
    if spacing and (i % spacing) == (spacing - 1):
        print('\t', end = '')

  print('') # Trailing blank line.

if __name__ == '__main__':
  moves = 32
  space_frequency = 4
  if len(sys.argv) > 1:
    try:
      moves = sys.argv[1]
      moves = abs(int(moves))
    except:
      print('Usage: $./shuffle.py [amount of shuffle moves] [frequency of spacing]')
      exit()
  if len(sys.argv) > 2:
    space_frequency = abs(int(sys.argv[2]))
  shuffle(moves, space_frequency)
