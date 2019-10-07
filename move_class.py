"""This module contains the class Move, for creating Rubik's cube moves.
For an explanation of Rubik's cube notation checkout the following article
in the Twisty puzzle wiki: https://ruwix.com/the-rubiks-cube/notation/
"""
import random

FACES = ('L', 'R', 'U', 'D', 'F', 'B')
CLOCKWISE_TURNS = (-1, 1, 2)  # Negative means anti-clockwise.

class Move:
    """A move on a Rubik's cube. Main properties are face and amount of clockwise turns."""
    def __init__(self, input_face=None, input_turns=None):
        # Init face (char)
        if not input_face:
            self.face = random.choice(FACES)
        elif input_face in FACES:
            self.face = input_face
        else:
            print('Illegal face chosen for Move object. Please use one from {}.'.format(FACES))
            exit()

        # Init clockwise_turns (integer)
        if not input_turns:
            self.clockwise_turns = random.choice(CLOCKWISE_TURNS)
        elif input_turns in CLOCKWISE_TURNS:
            self.clockwise_turns = input_turns
        else:
            print('Illegal clockwise turn count chosen for Move object. Please use one from {}.'.format(CLOCKWISE_TURNS))
            exit()

        # Init direction (string), is_clockwise & is_prime (booleans) and half_turn (string)
        self.half_turn = ''
        if self.clockwise_turns == -1:
            self.direction = '\''
            self.is_clockwise = False
        elif self.clockwise_turns > 0:
            if self.clockwise_turns == 2:
                self.half_turn = str(self.clockwise_turns)
            self.direction = ''
            self.is_clockwise = True

        # Assemble the move's name in cube notation (examples: R', F2, U...).
        self.name = self.cube_notation = self.face + self.direction + self.half_turn

    def is_prime(self):
        """Returns a boolean determining if the move is prime (counter-clockwise)."""
        return not self.is_clockwise

    def is_similar_to(self, other_move):
        """Returns a boolean stating the move is similar (can cancel out with) to other_move."""
        similar = False
        if self.face == other_move.face:
            similar = True
        return similar
