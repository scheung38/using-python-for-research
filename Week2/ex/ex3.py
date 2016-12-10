# Create a function possibilities(board) that returns a list of all
# positions (tuples) on the board that are not occupied (0). (Hint:
# numpy.where is a handy function that returns a list of indexes that
# meet a condition.)
# board is already defined from previous exercises. Call possibilities
# (board) to see what it returns!

import numpy as np
from Week2.ex.ex2 import create_board, place
# from .ex2 import create_board, place # This will cause relative import error?


def possibilities(b):
    """
    :param b:
    :return:
    """
    return np.where(b) == 0

if __name__ == '__main__':
    board = create_board()
    print(place(board, 1, (0, 0)))
    print(possibilities(board))

# [[ 1.  1.  1.]
#  [ 0.  0.  0.]
#  [ 0.  0.  1.]]

# False
