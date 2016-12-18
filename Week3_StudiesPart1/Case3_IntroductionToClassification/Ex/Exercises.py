# If the response is quantitative-- say, a number that measures weight or height,
# we call these problems regression problems.
# If the response is qualitative-- say, yes or no, or blue or green,
# we call these problems classification problems.

# From a mathematical perspective, it will be nicer to use column vectors
# but we'll be using row vectors, because they're easier to deal with in NumPy.

# Pseudo Code
#  Loop over all points
#    compute the distance between point p and every other point
# Python cannot handle import when name contains hyphens

import random

import numpy as np
import pandas as pd

from Week3_StudiesPart1.Case3_IntroductionToClassification.Ex.k_NearestNeighboursClassifier import knn_predict

data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")
# print(data)
#       fixed_acidity  volatile_acidity  citric_acid  residual_sugar  chlorides  \
# 0               7.4             0.700         0.00            1.90      0.076
# 1               7.8             0.880         0.00            2.60      0.098
# 2               7.8             0.760         0.04            2.30      0.092
# 3              11.2             0.280         0.56            1.90      0.075
# 4               7.4             0.700         0.00            1.90      0.076

# Ex2
# The dataset remains stored as data. Two columns in data are is_red and color,
# which are redundant. Drop color from the dataset, and save the new dataset as numeric_data.
numeric_data = data.drop("color", axis=1)

# Ex3
# To ensure that each variable contributes equally to the kNN classifier, we need to standardize the data. First, from each variable in numeric_data, subtract its mean. Second, for each variable in numeric_data, divide by its standard deviation. Store this again as numeric_data.
# Principal component analysis is a way to take a linear snapshot of the data from several different angles, with each snapshot ordered by how well it aligns with variation in the data. Use the PCA function in the scikit-learn (sklearn) library to find and store the two most informative principal components of the data (a matrix with two columns corresponding to the principal components), and store it as pca.
# Use the fit and transform methods on numeric_data to extract the first two principal components and store them as principal_components.
numeric_data = (numeric_data - np.mean(numeric_data, axis=0)) / np.std(numeric_data, axis=0)

import sklearn.decomposition

pca = sklearn.decomposition.PCA(2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

# Ex4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:, 0]
y = principal_components[:, 1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha=0.2,
            c=data['high_quality'], cmap=observation_colormap, edgecolors='none')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.xlabel("Principal Component 1");
plt.ylabel("Principal Component 2")
plt.show()


# Ex5
# We are now ready to fit the wine data to our kNN classifier. Create a function accuracy(predictions, outcomes) that takes two lists of the same size as arguments and returns a single number, which is the percentage of elements that are equal for the two lists.
# Use accuracy to compare the percentage of similar elements in x = np.array([1,2,3]) and y = np.array([1,2,4]).
# Print your answer.
def accuracy(predictions, outcomes):
    """
    Finds the percent of predictions that equal outcomes.
    """
    return 100 * np.mean(predictions == outcomes)


x = np.array([1, 2, 3])
y = np.array([1, 2, 4])

print(accuracy(x, y))

# Ex6
# The dataset remains stored as data. Because most wines in the dataset are classified as low quality, one very simple classification rule is to predict that all wines are of low quality. Use the accuracy function (preloaded into memory as defined in Exercise 5) to calculate how many wines in the dataset are of low quality.
# Print your result.
print(accuracy(0, data["high_quality"]))

# Ex7
# Use the scikit-learn classifier KNeighborsClassifier to predict which wines are high and low quality and store the result as library_predictions.
# Use accuracy to find the accuracy of library_predictions.
# Print your answer. Is this prediction better than the simple classifier in Exercise 6?
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions, data["high_quality"]))

# Ex8
# Unlike the scikit-learn function, our homemade kNN classifier does not take any shortcuts in calculating which neighbors are closest to each observation, so it is likely too slow to carry out on the whole dataset. To circumvent this, use random.sample and range(n_rows) to sample 10 row indices from the dataset. In this case, use seed 123 to select the row indices of your sample. Store this selection of indices as selection.
n_rows = data.shape[0]

random.seed(123)
selection = random.sample(range(n_rows), 10)

# Ex9
# Complete my_prediction with a numpy array. This array will contain predicted values of the wine's quality (i.e., like "high_quality" column in data). You need to use the knn_predict() function with k=5 to get these values from a subset of the data array (e.g., where indices match selection). Note that selection is already defined from Exercise 8, and knn_predict is already defined as in the Case 3 videos.
# Using the accuracy function, compare these results to the selected rows from the high_quality variable in data. Store these results as percentage.
# Print your answer.
predictors = np.array(numeric_data)
outcomes = np.array(data["high_quality"])
my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors[selection]])
percentage = accuracy(my_predictions, data.high_quality[selection])
print(percentage)
