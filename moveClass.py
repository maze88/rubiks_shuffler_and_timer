import random

faces = ('L', 'R', 'U', 'D', 'F', 'B')
clockwiseTurns = (-1, 1, 2)  # Negative means anti-clockwise.

class Move:
  """A move on a Rubik's cube. Main properties are face and amount of clockwise turns (cTurns)."""
  previousMove = 0

  def __init__(self, inputFace = 0, inputTurns = 0):
    try:
      print('Debug: previousMove = {}'.format(Move.previousMove.cubeNotation))
    except:
      pass
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
    print('Debug: created self = {}'.format(self.cubeNotation))

    # Check if move can be merged with previous move, if True, edit current move.
    if Move.previousMove:
      (similar, new_move) = Move.mergeMoves(self, Move.previousMove)
      if similar:
        self = new_move
        print('Debug: created new_move = {}'.format(new_move.cubeNotation))

    # For next move's instantiation.
    Move.previousMove = self

  def mergeMoves(moveA, moveB):
    """Returns a tuple containing False, unless a previous move exists which cancels out with it, and moveA (or a new move if boolean element was True)."""
    print('Debug: mergeMoves({}, {})'.format(moveA.cubeNotation, moveB.cubeNotation))
    mergable = False
    new_move = moveA
    if moveA.face == moveB.face:
      mergable = True
      new_face = moveA.face
      new_cTurns = moveA.cTurns + moveB.cTurns
      new_cTurns = abs(new_cTurns)
      if new_cTurns == 3:
        new_cTurns = -1
      if new_cTurns == 4:
        new_cTurns = 0
      new_move = Move()
      print('Debug: new_move = {}'.format(new_move.cubeNotation))
    return (mergable, new_move)
