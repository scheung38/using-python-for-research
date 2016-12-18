# Create a function possibilities(board) that returns a list of all
# positions (tuples) on the board that are not occupied (0). (Hint:
# numpy.where is a handy function that returns a list of indexes that
# meet a condition.)
# board is already defined from previous exercises. Call possibilities
# (board) to see what it returns!

import numpy as np
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex2 import create_board, place
# from .ex2 import create_board, place # This will cause relative import error?

# Ex3
def possibilities(brd):
    """
    :param brd:
    :return:
    """
    return list(zip(*np.where(brd == 0)))
    # return np.where(brd) == 0

if __name__ == '__main__':
    board = create_board()

    # Fill in positions where still zero
    print(place(board, 1, (0, 0)))
    # print(place(board, 1, (0, 1)))
    # print(place(board, 1, (0, 2)))
    # print(place(board, 1, (1, 0)))
    print(place(board, 1, (1, 1)))
    # print(place(board, 1, (1, 2)))
    # print(place(board, 1, (2, 0)))
    # print(place(board, 1, (2, 1)))
    print(place(board, 1, (2, 2)))

    # Get open positions still left
    print(possibilities(board))

# [[1 0 0]
#  [0 0 0]
#  [0 0 0]]

# [[1 0 0]
#  [0 1 0]
#  [0 0 0]]

# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# [(0, 1), (0, 2),
#  (1, 0), (1, 2),
#  (2, 0), (2, 1)]

