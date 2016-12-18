# Learn how to compare correlation matrices
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_2_loading_and_inspecting_data import whisky
from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_2_loading_and_inspecting_data import flavors
from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_3_exploring_correlations import corr_whisky
from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_4_clustering_whiskies_by_flavor_profile import model
from sklearn.cluster.bicluster import SpectralCoclustering

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize=(14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title('Original')
plt.axis("tight")

plt.subplot(122)
plt.pcolor(correlations)
plt.title('Rearrange')
plt.axis("tight")
plt.savefig('correlations.pdf')

# 4.1.5 Comparing Correlation Matrices
# Consider the following code:

import pandas as pd

data = pd.Series([1, 2, 3, 4])
data = data.ix[[3, 0, 1, 2]]
# What does data[0] return? Why?
print(data[0])
# 1 : data.ix alters the order of appearance, but leaves the indices the same.

# Consider the following code:

data = pd.Series([1,2,3,4])
data = data.ix[[3,0,1,2]]
data = data.reset_index(drop=True)
# What does data[0] return? Why?
print(data[0])
# 4 : The 0th index of the data has been reordered to
# index 3 of the original, which is 4.
