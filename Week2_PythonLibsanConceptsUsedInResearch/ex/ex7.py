# Create a similar function col_win(board, player) that takes the player (integer), and determines if any column consists of only their marker. Have it return True if this condition is met, and False otherwise.
# board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.

# Ex7
import numpy as np
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex2 import create_board, place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex3 import possibilities
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex4 import random_place

board = create_board()


def col_win(brd, player):
    winner = False
    if np.any(np.all(brd == player, axis=1)):
        return True
    else:
        return False
if __name__ == '__main__':
    print(col_win(board, 1))
