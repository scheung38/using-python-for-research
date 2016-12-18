# Create a function evaluate(board) that uses row_win, col_win, and diag_win functions for both players. If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
# board is already defined from previous exercises. Call evaluate to see if either player has won the game yet.

# Ex9
import numpy as np
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex2 import create_board, place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex3 import possibilities
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex4 import random_place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex5 import board
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex6 import row_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex7 import col_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex8 import diag_win


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0):
        winner = -1
    return winner


if __name__ == '__main__':
    evaluate(board)
