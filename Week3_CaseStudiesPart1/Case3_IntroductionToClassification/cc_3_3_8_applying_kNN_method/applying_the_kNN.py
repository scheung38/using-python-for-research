import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

from Week3_CaseStudiesPart1.Case3_IntroductionToClassification.Ex.k_NearestNeighboursClassifier import knn_predict
from Week3_CaseStudiesPart1.Case3_IntroductionToClassification.cc_3_3_6_making_a_prediction_grid.cc_3_3_6_making_prediction_grid import \
    make_prediction_grid

iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()

predictors = iris.data[:, 0:2]
outcomes = iris.target
plt.plot(predictors[outcomes == 0][:, 0], predictors[outcomes == 0][:, 1], 'ro')
plt.plot(predictors[outcomes == 1][:, 0], predictors[outcomes == 1][:, 1], 'go')
plt.plot(predictors[outcomes == 2][:, 0], predictors[outcomes == 2][:, 1], 'bo')
plt.savefig('iris.pdf')

k = 5;
filename = "iris_grid.pdf";
limits = (4, 8, 1.5, 4.5);
h = 0.1
xx, yy, prediction_grid = make_prediction_grid(predictors, outcomes, limits, h, k)
make_prediction_grid(xx, yy, prediction_grid, filename)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

print(sk_predictions.shape)
print(sk_predictions[0:10])

my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])
print(100*np.mean(sk_predictions == my_predictions))
# 96.0
print(100*np.mean(sk_predictions == outcomes))
# 83.33
print(100*np.mean(my_predictions == outcomes))
# 84.66

