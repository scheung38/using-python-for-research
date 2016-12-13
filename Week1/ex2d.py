# distance(x, y) is pre-loaded from part 2c.
# Make a function in_circle(x, origin) that uses distance to determine
# if a two-dimensional point falls within the the unit circle with a
# given origin. That is, find if a two-dimensional point has distance
# <1 from the origin (0,0).
# Use your function to print whether the point (1,1) lies within the
# unit circle centered at (0,0).

import numpy as np
from Week1.ex2c import distance

x = np.array([0, 0])
y = np.array([1, 1])

def in_circle(x, origin=[0]*2):

    # if point is inside circle return True
    # else return False
    if distance(x, origin)


print(in_circle(x, y))
