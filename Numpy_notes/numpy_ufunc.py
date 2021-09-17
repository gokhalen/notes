# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:56:58 2021

@author: User
"""

# https://www.w3schools.com/python/numpy/numpy_ufunc_create_function.asp

import numpy as np

def myadd(x, y):
  return x+y

# 2 - number of inputs
# 1 - number of outputs
myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(myadd))


# you get reductions and other special funcs for free

print(myadd.reduce([[1,1],[2,2],[2,2]]))

# also notice how in all examples we passed lists
# and they were all converted to np arrays