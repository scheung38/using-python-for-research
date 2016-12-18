import os
import numpy as np
import pandas as pd

# os.chdir('Week4_StudiesPart2/Case1_ClassifyingWhiskies/')
# Week4_StudiesPart2/Case1_ClassifyingWhiskies/c4_1_2_loading_and_inspecting_data.py

whisky = pd.read_csv("whiskies.txt")
# print(whisky)

whisky["Region"] = pd.read_csv("regions.txt")
# print(whisky["Region"])

print(whisky.head())

print(whisky.tail())


whisky.iloc[0:10]
whisky.iloc[5:10, 0:5]
whisky.columns

flavors = whisky.iloc[:, 2:14]

# 4_1_2
# What command reads in csv files in pandas ?
# pd.read_csv

