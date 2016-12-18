# For our tic-tac-toe board, we will use a numpy array with
# dimension 3 by 3. Make a function create_board() that creates
# such a board, with values of integers 0.
# Call create_board(), and store this as board

import numpy as np

board = np.zeros((3, 3))


# print('this is board type:')
# print(type(board))  # <class 'numpy.ndarray'>

def create_board(d):
    """
    :param d:
    :return: board
    """
    board = np.zeros((d, d))
    return board
    # pass


if __name__ == '__main__':
    print(create_board(3))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]
