import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

from Week3_StudiesPart1.Case3_IntroductionToClassification.Ex.k_NearestNeighboursClassifier import knn_predict
from Week3_StudiesPart1.Case3_IntroductionToClassification.cc_3_3_5_generating_synthetic_data import generate_synth_data
from Week3_StudiesPart1.Case3_IntroductionToClassification.cc_3_3_6_making_a_prediction_grid.cc_3_3_6_making_prediction_grid import \
    make_prediction_grid

predictors, outcomes = generate_synth_data()

k = 5; filename = "knn_synth_5.pdf"; limits = (-3, 4, -3, 4); h = 0.1
xx, yy, prediction_grid = make_prediction_grid(predictors, outcomes, limits, h, k)
make_prediction_grid(xx, yy, prediction_grid, filename)

k = 50; filename = "knn_synth_50.pdf"; limits = (-3, 4, -3, 4); h = 0.1
xx, yy, prediction_grid = make_prediction_grid(predictors, outcomes, limits, h, k)
make_prediction_grid(xx, yy, prediction_grid, filename)

# bias-variance tradeoff is choosing k to be between range

if __name__ == '__main__':
    print(predictors.shape)
    print(outcomes.shape)
