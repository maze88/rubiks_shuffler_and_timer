import random

faces = ('L', 'R', 'U', 'D', 'F', 'B')
clockwiseTurns = (-1, 1, 2)  # Negative means anti-clockwise.

class Move:
  """A move on a Rubik's cube. Main properties are face and amount of clockwise turns (cTurns)."""
  def __init__(self, inputFace = 0, inputTurns = 0):
    # Init face (char)
    if inputFace == 0:
      self.face = random.choice(faces)
    elif inputFace in faces:
      self.face = inputFace
    else:
      print('Illegal face chosen for Move object. Please use one from {}.'.format(faces))
      exit()

    # Init cTurns (integer)
    if inputTurns == 0:
      self.cTurns = random.choice(clockwiseTurns)
    elif inputTurns in clockwiseTurns:
      self.cTurns = inputTurns
    else:
      print('Illegal clockwise turn count chosen for Move object. Please use one from {}.'.format(clockwiseTurns))
      exit()

    # Init turnsCount (integers)
    self.turnsCount = abs(self.cTurns)

    # Init direction (string), isClockwise & isPrime (booleans) and halfTurn (string)
    self.halfTurn = ''
    if self.cTurns == -1:
      self.direction = '\''
      self.isClockwise = False
      self.isPrime = True
    elif self.cTurns > 0:
      if self.cTurns == 2:
        self.halfTurn = str(self.cTurns)
      self.direction = ''
      self.isClockwise = True
      self.isPrime = False

    # Assemble the move's name in cube notation (examples: R', F2, U...).
    self.cubeNotation = self.name = self.face + self.direction + self.halfTurn

    def cancelOut(self, moveB):
    """"""
      if self.face == moveB.face:
        new_cTurns = self.cTurns + moveB.cTurns
        if new_cTurns > 0:
          pass

        """
        -1-1=-2
        -1+1= 0
        -1+2= 1
         1+1= 2
         1+2= 3
         1-1= 0
         """


