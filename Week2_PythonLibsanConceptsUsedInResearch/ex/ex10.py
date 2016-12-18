# create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises. Create a function play_game() that creates a board, calls alternates between two players (beginning with Player 1), and evaluates the board for a winner after every placement. Play the game until one player wins (returning 1 or 2 to reflect the winning player), or the game is a draw (returning -1).
# Call play_game once.

# Ex10
import numpy as np
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex2 import create_board, place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex3 import possibilities
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex4 import random_place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex5 import board
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex6 import row_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex7 import col_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex8 import diag_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex9 import evaluate


def play_game():
    board, winner = create_board(), 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


if __name__ == '__main__':
    play_game()
