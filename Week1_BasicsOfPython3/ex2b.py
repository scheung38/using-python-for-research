# Using random.uniform, create a function rand() that generates a single float between -1 and 1.
# Call rand() once. So we can check your solution, we will use random.seed to fix the
# value called by your function.

import math
import random
import numpy as np


def rand():
    return np.random.uniform(-1.0, 1.0)


print(rand())

