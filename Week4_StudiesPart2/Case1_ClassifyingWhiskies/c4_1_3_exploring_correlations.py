# Learn how to explore correlations in your data
# Learn how to plot a correlation matrix

import pandas as pd
import matplotlib.pyplot as plt

from Week4_StudiesPart2.Case1_ClassifyingWhiskies.c4_1_2_loading_and_inspecting_data import flavors


corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig('corr_flavors.pdf')

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig('corr_whisky.pdf')


# How can you find a correlation matrix of a pd.Dataframe ?
# pd.Dataframe.corr

# How can you plot a correlation matrix by color?
# plt.pcolor correct

# What is the matplotlib.pyplot function that plots a colorbar on the side of a plot?
# plt.colorbar()