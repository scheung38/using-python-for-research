# Consider the following code:
import numpy as np

x = 20
print(not np.any([x % i == 0 for i in range(2, x)]))

# What does this return?
# False
