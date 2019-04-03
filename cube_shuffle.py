#!/usr/bin/python3

import random
import sys

faces = ('L', 'R', 'U', 'D', 'F', 'B')

class Move:
  """A move in a Rubik's cube shuffle. Main properties are face, direction and amount of turns."""
  def __init__(self, face = 'random', clockwiseTurns = 'random'):
    # Init face
    if face == 'random':
      self.face = random.choice(faces)
    elif face in faces:
      self.face = face
    else:
      print('Illegal face chosen for Move object. Please use one from {}.'.format(faces))
      exit()
    # Init turns
    if clockwiseTurns == 'random':
      self.turns = random.randint(1, 3)
    elif clockwiseTurns in (1, 2, 3):
      self.turns = clockwiseTurns
    else:
      print('Illegal clockwise turn count chosen for Move object. Please use 1, 2 or 3.')
      exit()

  def face(self):
    """Returns a single charactar, representing which face of the cube turns in move."""
    return self.face

  def direction(self):
    """Returns an [empty] string with the move's direction.
       Empty is clockwise, prime `'` is counter clockwise."""
    if clockwiseTurns == 2:
      return '\''
    else:
      return ''

  def turns(self):
    """Returns an integer of the amount of quarter turns in move."""
    if clockwiseTurns == 2:
      return clockwiseTurns
    else:
      return 1

  def isClockwise(self):
    """Returns True/False regarding direction of move's turn."""
    if direction(self):
      return False
    else:
      return True

  def isCounterClockwise(self):
    """Returns True/False regarding direction of move's turn."""
    if direction(self):
      return True
    else:
      return False

  def name(self):
    """Returns a string of the move's cube notation, example `L'`."""
    name = ''
    name += '' # todo
    return name


def main(n, spacing):
  print('Generating {} random moves...'.format(n))
  for move in range(n):
    if move % spacing == 0:
      print('')  # add spacing.
    print(randMove())
  print('') # trailing new line.

if __name__ == '__main__':
  moves = 25
  space_frequency = 5
  if len(sys.argv) > 1:
    moves = sys.argv[1]
    moves = abs(int(moves))
  if len(sys.argv) > 2:
    space_frequency = abs(int(sys.argv[2]))
  main(moves, space_frequency)
