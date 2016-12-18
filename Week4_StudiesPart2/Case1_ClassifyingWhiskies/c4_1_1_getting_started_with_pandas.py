# Pandas is a Python library that provides data structures and functions
# for working with structured data, primarily tabular data.
# Pandas is built on top of NumPy and some familiarity with NumPy
# makes Pandas easier to use and understand.
# Pandas has two data structures that you need to know the basics of,
# and these are called Series and Data Frame.

# In short, Series is a one-dimensional array-like object,
# and Data Frame is a two-dimensional array-like object.
# Both objects also contain additional information about the data
# called metadata, and this is something that
# will become clear through examples.

import pandas as pd

x = pd.Series([6, 3, 8, 6])
print(x)

x = pd.Series([6, 3, 8, 6], index=["q", "w", "e", "r"])
y = pd.Series([7, 3, 5, 2], index=["e", "q", "r", "t"])

print(x)

data = {
    'name': ['Time','Jim','Pam','Sam'],
    'age': [29,31,27,35],
    'ZIP': ['02155','02130','67700','00100']
}
print(pd.DataFrame(data))
print(pd.DataFrame(data, columns=['name', 'age', 'ZIP']))

print(x.index)
print(sorted(x.index))

print(x.reindex(sorted(x.index)))

print('this is x + y')
print(x+y)

# 4_1_1 Getting started with Pandas Q1

# What is Pandas?
# A Python library designed to query and manipulate annotated data tables

# What keyword allows you to specify names to indices in a pd.Series ?
# index

# In pandas , what does the reindex method do?
# Reorders the indices of a pandas Series object according to its argument