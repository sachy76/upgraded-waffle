# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:35:37 2024

@author: sachin
"""
# https://github.com/dask/dask-examples

from dask.distributed import Client, progress
client = Client(threads_per_worker=8, n_workers=1)
client


import time
import random

# Define function which needs parallel execution
def costly_simulation(list_param):
    time.sleep(random.random())
    return sum(list_param)

costly_simulation([1, 2, 3, 4])


# Define input which will go as parameter into above function
import pandas as pd
import numpy as np
input_params = pd.DataFrame(np.random.random(size=(500, 4)),
                            columns=['param_a', 'param_b', 'param_c', 'param_d'])
input_params.head()
results = []

# Execute function without parallel mode
for parameters in input_params.values[:20]:
    result = costly_simulation(parameters)
    results.append(result)
    print(results)
    

# Use Dask Delayed to make our function lazy
import dask
lazy_results = []
for parameters in input_params.values:
    lazy_result = dask.delayed(costly_simulation)(parameters)
    lazy_results.append(lazy_result)
futures = dask.persist(*lazy_results)  # trigger computation in the background
#print(lazy_result)
    

# Execute with Dask Parallel by calling compute
results = dask.compute(*lazy_results)
print(results[:5])




# Using Dask Futures API
futures = []
for parameters in input_params.values:
    future = client.submit(costly_simulation, parameters)
    futures.append(future)
results = client.gather(futures)
print(len(results))
print(results[:5])

