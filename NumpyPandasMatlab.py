# This is session 5 Lab for Numpy Pandas
import pandas as pd
import numpy as np

# print("Pandas Version", pd.__version__)
# print("Numpy Version", np.__version__)
# What is Series - 1D labeled homogeneously-typed array
# What is DataFrame -
# DataFrame - General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column
# series = pd.Series(data, index=index)
# <b>From Python dict <br></b>

# Series can be instantiated from dicts:
"""
dict = {"key1": 1, "key2": 1, "key3": 2}
print(dict)

series = pd.Series(dict)

print("Series elements : ")
print(series)

print("\n data type : ", type(series))

print("\n data type of series elements: ", series.dtype)

print("\n number of series elements : ", len(series))

# If data is a ndarray, index must be the same length as data. If no index is passed, one will be created having
# values [0, ..., len(data) - 1].

array = np.array([10, 23, 34, 45, 45])
series = pd.Series(array)
print(series)


array = np.array([12, 23, 45, 56, 56])
index = ["a", "b", "c", "d", "e"]
series = pd.Series(array, index)
print(series)

# If data is a scalar value, an index must be provided. The value will be repeated to match the length of index.
series = pd.Series(1., index=['a', 'b', 'c'])
print(series)
"""

# DataFrame
"""
DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it 
like a spreadsheet or SQL table, or a dictionary of Series objects. 
It is generally the most commonly used pandas object. 
Like Series, DataFrame accepts many different kinds of input: <br>

- Dictionary of Series, 1D ndarrays, lists, dicts
- 2-D numpy.ndarray
- Structured or record ndarray
- A Series
- Another DataFrame <br>

Along with the data, you can optionally pass index (row labels) and columns (column labels) arguments.
"""
# The data frame can be created from dictionary object which holds series as its values. Here dictionary contains four
# series in it like name, age, salary and working with corresponding data values in it.
dict = {
           "name" : pd.Series(["A", "B", "c"]),
           "age": pd.Series([21, 22, 23]),
           "salary": pd.Series([11.5, 23.4, 56]),
           "working" : pd.Series([True, False, True])
       }
print(dict)