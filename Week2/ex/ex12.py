# This result is expected --- when guessing at random, it's better to go first. Let's see if Player 1 can improve their strategy. create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises. Create a function play_strategic_game(), where Player 1 always starts with the middle square, and otherwise both players place their markers randomly.
# Call play_strategic_game once.

# Ex12
import matplotlib.pyplot as plt
import numpy as np
from Week2.ex.ex2 import create_board, place
from Week2.ex.ex3 import possibilities
from Week2.ex.ex4 import random_place
from Week2.ex.ex5 import board
from Week2.ex.ex6 import row_win
from Week2.ex.ex7 import col_win
from Week2.ex.ex8 import diag_win
from Week2.ex.ex9 import evaluate
from Week2.ex.ex10 import play_game


def play_strategic_game():
    board, winner = create_board(), 0
    board[1, 1] = 1
    while winner == 0:
        for player in [2, 1]:
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


if __name__ == '__main__':
    play_strategic_game()
