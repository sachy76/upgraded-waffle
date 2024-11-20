# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:22:15 2024

@author: sachin
"""
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# set this so the 
%matplotlib inline

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')
chipo.head(10)

# Create a histogram of the top 5 items bought
# get the Series of the names
x = chipo.item_name
# use the Counter class from collections to create a dictionary with keys(text) and frequency
letter_counts = Counter(x)
# convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(letter_counts, orient='index')
# sort the values from the top to the least value and slice the first 5 items
df = df[0].sort_values(ascending = True)[45:50]
# create the plot
df.plot(kind='bar')
# Set the title and labels
plt.xlabel('Items')
plt.ylabel('Number of Times Ordered')
plt.title('Most ordered Chipotle\'s Items')
# show the plot
plt.show()

# Create a scatterplot with the number of items orderered per order price
# create a list of prices
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space

# then groupby the orders and sum
orders = chipo.groupby('order_id').sum()

# creates the scatterplot
# plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green')
plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')

# Set the title and labels
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)
plt.show()