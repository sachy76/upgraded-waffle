# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:10:14 2024

@author: sachin
"""
import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep = '\t')


# How many products cost more than $10.00?
prices = [float(value[1 : -1]) for value in chipo.item_price]

chipo.item_price = prices

chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])

chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
chipo_one_prod

chipo_one_prod[chipo_one_prod['item_price']>10].item_name.nunique()



# What is the price of each item? print a data frame with only two columns item_name and item_price

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])
chipo[(chipo['item_name'] == 'Chicken Bowl') & (chipo['quantity'] == 1)]

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

# select only the item_name and item_price columns
price_per_item = chipo_one_prod[['item_name', 'item_price']]

# sort the values from the most to less expensive
price_per_item.sort_values(by = "item_price", ascending = False).head(20)



# Sort by the name of the item
chipo.item_name.sort_values()
chipo.sort_values(by = "item_name")

# What was the quantity of the most expensive item ordered?
chipo.sort_values(by = "item_price", ascending = False).head(1)


# How many times was a Veggie Salad Bowl ordered?
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]
len(chipo_salad)

# How many times did someone order more than one Canned Soda?
chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)