# If the response is quantitative-- say, a number that measures weight or height,
# we call these problems regression problems.
# If the response is qualitative-- say, yes or no, or blue or green,
# we call these problems classification problems.

# From a mathematical perspective, it will be nicer to use column vectors
# but we'll be using row vectors, because they're easier to deal with in NumPy.

# Pseudo Code
#  Loop over all points
#    compute the distance between point p and every other point
import matplotlib.pyplot as plt
import numpy as np

from Week3_StudiesPart1.Case3_IntroductionToClassification.cc_3_3_1_intro_to_kNN_classification.Introduction_to_kNN_Classification import \
    distance
from Week3_StudiesPart1.Case3_IntroductionToClassification.cc_3_3_1_intro_to_kNN_classification.MajorityVote import \
    majority_vote

points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
p = np.array([2.5, 2])


def find_nearest_neighbors(p, points, k=5):
    """
    Find the k nearest neighbors of point p and return their indices
    :param p:
    :param points:
    :param k:
    :return:
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    # Two nearest points to p
    print('The two nearest points to p are')
    return ind[0:k]
    # return ind[:k] same as above
    # sort distances and return those k points that are nearest to point p


ind = find_nearest_neighbors(p, points, 2)
print(points[ind])
# The two nearest points to p are
# [[2 2]
#  [3 2]]

ind = find_nearest_neighbors(p, points, 3)
print(points[ind])


# The two nearest points to p are
# [[2 2]
#  [3 2]
#  [2 1]]


def knn_predict(p, points, outcomes, k=5):
    # find k nearest neighbours
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])
    # predict the class of p based on majority vote


outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
print(len(outcomes))

print('knn_predict is')
print(knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2))
# 1
print('knn_predict is')
print(knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2))
# 0

# For the x-coordinates, we would like to plot all of the rows in column 0,
# and the y-coordinates correspond to all of the rows in column 1.
plt.plot(points[:, 0], points[:, 1], 'ro')
plt.plot(p[0], p[1], 'bo')
plt.axis([0.5, 3.5, 0.5, 3.5])
plt.show()
