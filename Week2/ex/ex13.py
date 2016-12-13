# The results from Exercise 12 have been stored. Use the play_strategic_game() function to play 1,000 random games.
# Use the time libary to evaluate how long all these games takes.
# The library matplotlib.pyplot has already been stored as plt. Use plt.hist and plt.show to plot your results. Did Player 1's performance improve? Does either player win more than each player draws?

# Ex13

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
from Week2.ex.ex12 import play_strategic_game

import time
start = time.time()
games = [play_strategic_game() for i in range(1000)]
stop = time.time()
print(stop - start)
plt.hist(games)
plt.show()
