# How does the k-Nearest Neighbors classifier classify observations?
# According to the most common class among the nearest k neighbors
import numpy as np


def distance(p1, p2):
    """
    Fine the distance between 2 points
    :param p1:
    :param p2:
    :return:
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

if __name__ == '__main__':
    p1 = np.array([1, 1])
    p2 = np.array([4, 4])

    print(distance(p1, p2))
    # 4.24264068712
