# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

a = np.arange(12).reshape(3,4)

# i an j must have the same equal shape
i = np.array([[0,1],
              [1,2]])

j = np.array([[2,1],
              [3,3]])

# combines each element in i and j to get a indexing tuple
# so the elements of a[i,j] are 
# a[0,2] a[1,1]
# a[1,3] a[3,2]
print(a[i,j])
print('-'*40)
# broadcasts '2' into the shape of i and proceeds as before
print(a[i,2])
print('-'*40)
# return a[1,j], a[2,j], a[3,j]
# 1,2,3 will be broadcasted to match the shape of j
print(a[:,j])