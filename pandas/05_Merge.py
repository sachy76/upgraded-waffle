# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:57:30 2024

@author: sachin
"""

import pandas as pd
import numpy as np

s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

print(s1, s2, s3)

# Let's create a DataFrame by joinning the Series by column
housemkt = pd.concat([s1, s2, s3], axis=1)
housemkt.head()

# Change the name of the columns to bedrs, bathrs, price_sqr_meter
housemkt.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
housemkt.head()

# Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'
bigcolumn = pd.concat([s1, s2, s3], axis=0)

bigcolumn = bigcolumn.to_frame()
print(type(bigcolumn))

bigcolumn

# Oops, it seems it is going only until index 99. Is it true?
len(bigcolumn)

# Reindex the DataFrame so it goes from 0 to 299
bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn