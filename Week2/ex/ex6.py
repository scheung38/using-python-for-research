# Now that players may place their pieces, how will they know they've won? Make a function row_win(board, player) that takes the player (integer), and determines if any row consists of only their marker. Have it return True of this condition is met, and False otherwise.
# board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.

# Ex6
import numpy as np
from Week2.ex.ex2 import create_board, place

# from Week2.ex.ex3 import possibilities
# from Week2.ex.ex4 import random_place

board = create_board()


def row_win(brd, player):
    winner = False
    if np.any(np.all(brd == player, axis=1)):
        return True
    else:
        return False


if __name__ == '__main__':
    print(row_win(board, 1))
