# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:34:29 2024

@author: sachin
"""


import pandas as pd

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()

# Which continent drinks more beer on average?
drinks.groupby('continent').beer_servings.mean()

# For each continent print the statistics for wine consumption.
drinks.groupby('continent').wine_servings.describe()

# Print the mean, min and max values for spirit consumption.
drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])

