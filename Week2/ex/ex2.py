# Players 1 and 2 will take turns changing values of this array
# from a 0 to a 1 or 2, indicating the number of the player who
# places there. Create a function place(board, player, position)
# with player being the current player (an integer 1 or 2), and
# position a tuple of length 2 specifying a desired location to
# place their marker. Only allow the current player to place a
# piece on the board (change the board position to their number)
# if that position is empty (zero).

# Use create_board() to store a board as board, and use place to
# have Player 1 place a piece on spot (0, 0).
import numpy as np


# board = np.zeros((3, 3))


def create_board():
    """
    :return:
    """
    return np.zeros((3, 3))


def place(board, player, position):
    """
    :param board: this is playing area
    :param player: this is current player, 1 or 2
    :param position: a tuple of length 2 specifying desired location to place marker
    :return:
    """
    if board[position] == 0:
        board[position] = player

    return board

if __name__ == '__main__':

    board = create_board()
    print(place(board, 1, (0, 0)))

# [[ 1.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]

    print(place(board, 1, (0, 1)))

# [[ 1.  1.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]

    print(place(board, 1, (0, 2)))

# [[ 1.  1.  1.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]

    print(place(board, 1, (2, 2)))

# [[ 1.  1.  1.]
#  [ 0.  0.  0.]
#  [ 0.  0.  1.]]



