# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:34:47 2024

@author: sachin
"""

import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

%matplotlib inline

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

apple.head()

apple.dtypes

# Transform the Date column as a datetime type
apple.Date = pd.to_datetime(apple.Date)
apple['Date'].head()

# Set the date as the index
apple = apple.set_index('Date')
apple.head()

# Is there any duplicate dates?
# NO! All are unique
apple.index.is_unique

# Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
apple.sort_index(ascending = True).head()

# Get the last business day of each month
apple_month = apple.resample('BM').mean()

apple_month.head()

# What is the difference in days between the first day and the oldest
(apple.index.max() - apple.index.min()).days

# How many months in the data we have?
apple_months = apple.resample('BM').mean()

len(apple_months.index)

# Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
# makes the plot and assign it to a variable
appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)
