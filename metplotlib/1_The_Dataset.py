# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:46:12 2024

@author: sachin
"""

#https://www.datacamp.com/tutorial/matplotlib-tutorial-python

import pandas as pd

djia_data = pd.read_csv('C:/Users/sachin/workspace/upgraded-waffle/metplotlib/HistoricalPrices.csv')
djia_data = djia_data.rename(columns = {' Open': 'Open', ' High': 'High', ' Low': 'Low', ' Close': 'Close'})
djia_data.head()

djia_data['Date'] = pd.to_datetime(djia_data['Date'])
djia_data = djia_data.sort_values(by = 'Date')


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# Line Plots with a Single Line
plt.plot(djia_data['Date'], djia_data['Close'])
plt.show()

# Line Plots with Multiple Lines
plt.plot(djia_data['Date'], djia_data['Open'])
plt.plot(djia_data['Date'], djia_data['Close'])
plt.show()

# Adding a Legend
plt.plot(djia_data['Date'], djia_data['Open'], label = 'Open')
plt.plot(djia_data['Date'], djia_data['Close'], label = 'Close')
plt.legend()
plt.show()

# Drawing Bar Plots
# Import the calendar package 
from calendar import month_name

# Order by months by chronological order
djia_data['Month'] = pd.Categorical(djia_data['Date'].dt.month_name(), month_name[1:])

# Group metrics by monthly averages
djia_monthly_mean = djia_data \
    .groupby('Month') \
    .mean() \
    .reset_index()
djia_monthly_mean.head(6)

# Vertical Bar Plots
plt.bar(djia_monthly_mean['Month'], height = djia_monthly_mean['Close'])
plt.show()

# Reordering Bars in Bar Plots
djia_monthly_mean_srtd = djia_monthly_mean.sort_values(by = 'Close', ascending = False)

plt.bar(djia_monthly_mean_srtd['Month'], height = djia_monthly_mean_srtd['Close'])
plt.show()

# Horizontal Bar Plots
#plt.barh(djia_monthly_mean_srtd['Month'], height = djia_monthly_mean_srtd['Close'])
#plt.show()


# Drawing Scatter Plots
plt.scatter(djia_data['Open'], djia_data['Close'])
plt.show()

# Scatter Plots with a Trend Line
z = np.polyfit(djia_data['Open'], djia_data['Close'], 1)
p = np.poly1d(z)


plt.scatter(djia_data['Open'], djia_data['Close'])
plt.plot(djia_data['Open'], p(djia_data['Open']))
plt.show()

# Setting the Plot Title and Axis Labels
plt.scatter(djia_data['Open'], djia_data['Close'])
plt.show()

# Changing Colors
plt.plot(djia_data['Date'], djia_data['Open'], color = 'black')
plt.plot(djia_data['Date'], djia_data['Close'], color = 'red')
plt.show()

plt.bar(djia_monthly_mean_srtd['Month'], height = djia_monthly_mean_srtd['Close'], color = ['blue', 'gray', 'gray', 'gray', 'gray', 'gray'])
plt.show()

plt.scatter(djia_data[djia_data['Month'] == 'January']['Open'], djia_data[djia_data['Month'] == 'January']['Close'], color = 'blue')

plt.scatter(djia_data[djia_data['Month'] != 'January']['Open'], djia_data[djia_data['Month'] != 'January']['Close'], color = 'gray')

plt.show()


# Saving Plots
plt.scatter(djia_data['Open'], djia_data['Close'])
plt.savefig('DJIA 2022 Scatterplot Open vs. Close.png')


