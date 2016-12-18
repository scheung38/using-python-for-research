# Use the play_game() function to play 1,000 random games, where Player 1 always goes first.
# When doing this, import and use the time library to call the time function both before and after playing all 1,000 games in order to evaluate how long this takes per game. Print your answer.
# The library matplotlib.pyplot has already been stored as plt. Use plt.hist and plt.show to plot a histogram of the results. Does Player 1 win more than Player 2? Does either player win more than each player draws?

# Ex11
import matplotlib.pyplot as plt
import numpy as np
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex2 import create_board, place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex3 import possibilities
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex4 import random_place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex5 import board
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex6 import row_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex7 import col_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex8 import diag_win
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex9 import evaluate
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex10 import play_game

if __name__ == '__main__':
    import time

    start = time.time()
    games = [play_game() for i in range(1000)]
    stop = time.time()
    print(stop - start)
    plt.hist(games)
    plt.show()
