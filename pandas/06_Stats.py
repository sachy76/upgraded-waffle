# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:08:15 2024

@author: sachin
"""

import pandas as pd

baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()
baby_names.head(10)

# Delete the column 'Unnamed: 0' and 'Id'

del baby_names['Unnamed: 0']
del baby_names['Id']
baby_names.head()

# Are there more male or female names in the dataset?
baby_names['Gender'].value_counts()

# Group the dataset by name and assign to names
del baby_names["Year"]
names = baby_names.groupby("Name").sum()
names.head()
names.sort_values("Count", ascending = 0).head()

# How many different names exist in the dataset?
len(names)

# What is the name with most occurrences?
names.Count.idxmax()

# How many different names have the least occurrences?
len(names[names.Count == names.Count.min()])

# What is the median name occurrence?
names[names.Count == names.Count.median()]

# What is the standard deviation of names?
names.Count.std()

# Get a summary with the mean, min, max, std and quartiles.
names.describe()

