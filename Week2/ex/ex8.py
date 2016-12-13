# Finally, create a function diag_win(board, player) that tests if either diagonal of the board consists of only their marker. Have it return True if this condition is met, and False otherwise.
# board is already defined from previous exercises. Call diag_win to check if Player 1 has a complete diagonal.


# Ex8
import numpy as np
from Week2.ex.ex2 import create_board, place
from Week2.ex.ex3 import possibilities
from Week2.ex.ex4 import random_place

board = create_board()


def diag_win(board, player):
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    else:
        return False

if __name__ == '__main__':
    print(diag_win(board, 1))
