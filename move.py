import random

faces = ('L', 'R', 'U', 'D', 'F', 'B')
clockwiseTurns = (-1, 1, 2)  # Negative mean anti-clockwise.

class Move:
  """A move on a Rubik's cube. Main properties are face and amount of clockwise turns (cTurns)."""
  def __init__(self, inputFace = 'random', inputTurns = 'random'):
    # Init face (char)
    if inputFace == 'random':
      self.face = random.choice(faces)
    elif inputFace in faces:
      self.face = inputFace
    else:
      print('Illegal face chosen for Move object. Please use one from {}.'.format(faces))
      exit()

    # Init cTurns (integer)
    if inputTurns == 'random':
      self.cTurns = random.choice(clockwiseTurns)
    if inputTurns in clockwiseTurns:
      self.cTurns = inputTurns
    else:
      print('Illegal clockwise turn count chosen for Move object. Please use one from {}.'.format(clockwiseTurns))
      exit()

    # Init direction (string), isClockwise and isPrime (booleans)
    if self.cTurns < 0:
      self.direction = '\''
      self.isClockwise = False
      self.isPrime = True
    elif self.cTurns > 0:
      self.direction = ''
      self.isClockwise = True
      self.isPrime = False

    # Init halfTurn (string)
    if self.cTurns == 2:
      self.halfTurn = '2'
    else:
      self.halfTurn = ''

    # Init turnsCount (integers)
    self.turnsCount = abs(self.cTurns)

    # Assemble the move's name in cube notation (examples: R', F2, U...).
    self.cubeNotation = self.face + self.direction + self.halfTurn

