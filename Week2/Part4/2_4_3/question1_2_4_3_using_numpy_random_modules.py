# Consider the following code:
import numpy as np
import matplotlib.pyplot as plt

print(np.random.random((5, 2, 3)))
# Generate a 5 x 2 x 3 NumPy array with random uniform values

print('x' * 40)

print(np.random.normal(1, 2, 3))
# Generate 3 samples with mean 1 and standard deviation 2

print('x' * 40)

print(np.random.randint(1, 5, (2, 3)))
# Generate a 2 x 3 array with random integers from 1-4

print('x' * 40)

res = np.sum(np.random.randint(1, 7, (100, 10)), axis=0)

print(res)
# dimension is
# 10
