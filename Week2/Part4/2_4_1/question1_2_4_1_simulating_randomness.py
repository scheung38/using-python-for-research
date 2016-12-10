# Consider the following code:
import numpy as np
import matplotlib.pyplot as plt

print(np.random.choice(range(0, 10)))

print(np.random.choice(list([1, 2, 3, 4])))

print(sum(np.random.choice(range(10), 10)))

print(sum(np.random.choice(range(10)) for i in range(10)))
