# Learn how to use spectral co-clustering to cluster whiskies based on their flavor profiles

# The specific method we'll be using is called spectral co-clustering.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_2_loading_and_inspecting_data import flavors
from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_3_exploring_correlations import corr_whisky

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)

# Spectrum is in eigenvalues and eigenvectors

model.fit(corr_whisky)
model.rows_

np.sum(model.rows_, axis=0)
model.row_labels_


# What is spectral co-clustering?
# A method for finding clusters of objects by the similarity of their attributes

# How many clusters do we find in the whisky dataset used in Video 4.1.4?
# 6

