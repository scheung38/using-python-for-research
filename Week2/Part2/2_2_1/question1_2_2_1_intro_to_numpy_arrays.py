# Consider the following code:
import numpy as np

zero_vector = np.zeros(5)
print(zero_vector)

zero_matrix = np.zeros((3, 3))
print('zero_matrix is:')
print(zero_matrix)

empty_matrix = np.empty((3, 3))
print('empty_matrix is:')
print(empty_matrix)

A = np.array([[1, 3], [5, 9]])
B = np.array([[3, 3]])

print('A is : ')
print(A)
print('B is : ')
print(B)

print(A.transpose())


# True or False: a numpy array's length may be edited after being created.
# False

# Get info from commandline
# np.info(np.add)