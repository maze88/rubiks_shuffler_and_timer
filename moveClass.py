import random

faces = ('L', 'R', 'U', 'D', 'F', 'B')
clockwiseTurns = (-1, 1, 2)  # Negative means anti-clockwise.

class Move:
  """A move on a Rubik's cube. Main properties are face and amount of clockwise turns (cTurns)."""
  __previousMove = 0
  print('Debug: __previousMove = {}'.format(__previousMove))

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

    if Move.__previousMove:
      (merged, new_move) = mergeMoves(self, Move.__previousMove)

    # For next move's instantiation.
    __previousMove = self

  def mergeMoves(moveA, moveB):
    """Returns a tuple containing False, unless a previous move exists which cancels out with it, and itmoveA or a new move (based on boolean result)."""
    print('Debug: mergeMoves({}, {})'.format(moveA.cubeNotation, moveB.cubeNotation))
    mergable = False
    new_move = moveA
    if moveA.face == moveB.face:
      mergable = True
      new_face = moveA.face
      new_cTurns = moveA.cTurns + moveB.cTurns
      new_cTurns = abs(new_cTurns)
      if new_cTurns > 2:
        new_cTurns = -1
      new_move = Move(new_face, new_cTurns)
      print('Debug: new_move = {}'.format(new_move.cubeNotation))
    return (mergable, new_move)

