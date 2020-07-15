# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:57:56 2020

@author: Nachiket Gokhale

Difference between a[:,2] and a[:][2]

From https://stackoverflow.com/questions/62908171/query-about-picking-values-from-numpy-array

"""

import numpy as np
a = np.arange(9).reshape(3,3)

print(a)
print('-'*40)

# Row doesn't matter. So, for each row return the second element
print(a[:,2])
print('-'*40)

# the way subscripting works a[:] is evaluated first 
# which returns an object and then
# the [2] is applied to to that object
# a[:]  returns a itself because a[:] matches all all rows
# then [2] is applied to a itself, which means return the second row
print(a[:][2])
print('-'*40)
# the following means return the 0th and the 1st row, and then return the 
# 1st row
print(a[0:2][1])
