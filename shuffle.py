#!/usr/bin/python3

import random
import sys
from moveClass import Move

def recycleIfSimilar(currentMove, previousMove):
  """If currentMove and previousMove are similar (can cancel out), it generates a new currentMove. Returns currentMove."""
  if previousMove and currentMove.isSimilarTo(previousMove):
    previousMove = currentMove
    currentMove = recycleIfSimilar(Move(), currentMove)
  return currentMove

def shuffle(moves = 32, spacing = 4):
  previousMove = 0
  print('\nGenerating {} random moves...'.format(moves))
  for i in range(moves):
    move = recycleIfSimilar(Move(), previousMove)
    previousMove = move
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
