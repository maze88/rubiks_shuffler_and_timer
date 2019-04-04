#!/usr/bin/python3

import random
import sys

faces = ('L', 'R', 'U', 'D', 'F', 'B')

class Move:
  """A move in a Rubik's cube shuffle. Main properties are face, direction and amount of turns."""
  def __init__(self, face = 'random', cTurns = 'random'):
    # Init face (char)
    if face == 'random':
      self.face = random.choice(faces)
    elif face in faces:
      self.face = face
    else:
      print('Illegal face chosen for Move object. Please use one from {}.'.format(faces))
      exit()

    # Init turns (integers)
    if cTurns == 'random':
      self.__clockwiseTurns = random.randint(1, 3)
    elif clockwiseTurns in (1, 2, 3):
      self.__clockwiseTurns = cTurns
    else:
      print('Illegal clockwise turn count chosen for Move object. Please use 1, 2 or 3.')
      exit()

    # Init direction (primality string)
    if self.__clockwiseTurns == 3:
      self.direction = '\''
    else:
      self.direction = ''

    # Init turnsCount (integers)
    if not self.__clockwiseTurns == 2:
      self.turnsCount = 1
    else:
      self.turnsCount = self.__clockwiseTurns

    # Init isClockwise and isPrime (boolean)
    if self.__clockwiseTurns == 3:
      self.isClockwise = False
      self.isPrime = True
    else:
      self.isClockwise = True
      self.isPrime = False

    # Init halfTurn (char)
    if self.__clockwiseTurns == 2:
      self.halfTurn = '2'
    else:
      self.halfTurn = ''

    # Assemble the move's name in cube notation (examples: R', F2, U...).
    self.cubeNotation = self.face + self.direction + self.halfTurn


def main(n, spacing):
  print('Generating {} random moves...'.format(n))
  for m in range(n):
    move = Move()
    if m % spacing == 0:
      print('')  # add spacing.
    print(move.cubeNotation)
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
