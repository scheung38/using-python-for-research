# Consider the following code:
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4, 5])
b[a]

# What does this return?
# ValueError: operands could not be broadcast together with shapes (2,) (3,)
# np.array([4,5])

c = b[1:]
print(c)
# [4 5]
print(b[a])
# [4 5]
print(b[a] is c)
# False

