# The distance between two points x and y is the square root of the
# sum of squared differences along each dimension of x and y. Create
# a function distance(x, y) that takes two vectors and outputs the
# distance between them. Use your function to find the distance between
# (0,0) and (1,1).
# Print your answer.

import numpy as np

x = np.array([0, 0])
y = np.array([1, 1])
print(x)
print(y)


def distance(x, y):
    return np.sqrt(sum(y - x))


print(distance(x, y))
# 1.41421356237
