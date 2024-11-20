# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:45:12 2024

@author: sachin
"""

import pandas as pd
import numpy

csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
df.head()

# slice the dataframe from 'school' until the 'guardian' column
stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()


# Create a lambda function that will capitalize strings.
capitalizer = lambda x: x.capitalize()

# Capitalize both Mjob and Fjob
stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

# Print the last elements of the data set.
stud_alcoh.tail()

# Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(capitalizer)
stud_alcoh.tail()

# Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(x):
    if x > 17:
        return True
    else:
        return False
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
stud_alcoh.head()

# Multiply every number of the dataset by 10.
def times10(x):
    if type(x) is int:
        return 10 * x
    return x
stud_alcoh.applymap(times10).head(10)


