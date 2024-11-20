# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:18:56 2024

@author: sachin
"""

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url,sep='\t')

#see first 10 records
print(chipo.head(10))

#Size of data
print(chipo.shape[0])
print(chipo.info())

#Number of columns in dataset
print(chipo.shape[1])

# how is the data indexed
print(chipo.index)

# which was the most ordered item
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending = False)
print(c.head(1))

# for the most ordered item, how many items were ordered ?
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending = False)
print(c.head(1))

# What was the most oredered item in the choice_description columne ?
c = chipo.groupby('choice_description').sum()
c = c.sort_values(['quantity'],ascending = False)
print(c.head(1))

# how many items were ordered in total ?
total_items_orders = chipo.quantity.sum()
print(total_items_orders)

# Turn the item price into float
print(chipo.item_price.dtype)

dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)
print(chipo.item_price.dtype)

# How much was revenue
revenue = (chipo['quantity'] * chipo['item_price']).sum()
print('Revenue was: $' +str(np.round(revenue,2)))

# How many orders were made in perioid
orders = chipo.order_id.value_counts().count()
print(orders)

# How many different items were sold
print(chipo.item_name.value_counts().count())
