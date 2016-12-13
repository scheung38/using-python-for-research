# board is already defined from previous exercises. Use random_place(board, player)
# to place three pieces on board each for players 1 and 2.
# Print board to see your result.

# Ex5
import numpy as np
from Week2.ex.ex2 import create_board, place
from Week2.ex.ex3 import possibilities
from Week2.ex.ex4 import random_place

board = create_board()

for i in range(3):
    for player in [1, 2]:
        # add here!
        random_place(board, player)

print(board)






