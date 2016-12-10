# Create a function random_place(board, player) that places a
# marker for the current player at random among all the available
# positions (those currently set to 0).
# board is already defined from previous exercises. Call random_
# place(board, player) to place a random marker for Player 2, and
# store this as board to update its value.


# Ex4
import numpy as np
from Week2.ex.ex1 import board
from Week2.ex.ex2 import create_board, place
from Week2.ex.ex3 import possibilities


def random_place(board, player):
    """
    :param board: current board status
    :param player: current player (integer 1 or 2)
    :return: next board status
    """

    return board


if __name__ == '__main__':

    board = create_board()
    print('this is board initial setup:')
    print(board)
    print('this is place with player1')
    print(place(board, 1, (0, 0)))
    print('these are remaining spaces:')
    print(possibilities(board))
    print('next random move by player 2:')
    print(random_place(board, 2))