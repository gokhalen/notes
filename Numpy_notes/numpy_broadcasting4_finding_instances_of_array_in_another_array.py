# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:23:51 2020

@author: aa
"""

import numpy as np

# https://stackoverflow.com/questions/64890422/np-where-checking-also-for-subelements-in-multidimensional-arrays

# We need to check if a row in x is a row in z

x = np.array([[0,1,2,3], [4,0,6,9]])
z= np.array([[0,1,2,3], [5, 11, 6,98]])

# orgoro's answer

duplicates = (x[:, None] == z).all(-1).any(-1)

# let's analyze this a bit 

# this reshapes X i.e. increases the dimension by 1
# x.shape = (2,4), bb.shape = (2,1,4)
bb = x[:,None]

# now, broadcasting magic
# bb == z
# bb is reshaped to (2,2,4) and zz is reshaped to (2,2,4)
# cc[i,j,k] = bb_reshape[i,j,k] == zz_reshape[i,j,k]
#           = bb_reshape[i,0,k] == zz_reshape[0,j,k]
#           = x[i,k] == z[j,k]
# this means the difference between ith row of x and jth row of z
# is stored in cc[i,j,:]
cc = (bb == z)

# so to check if the 1st row of x is in z we can do
print(cc[0,:,:].all(axis=-1))
# to check the 2nd row of  is in z we can do
print(cc[1,:,:].all(axis=-1))
print('-'*80)
# or we can combine this more elegantly
print(cc.all(axis=-1))
# now if we do an 'any' on this we will get if the ith row of x is in z
duplicates2 = cc.all(axis=-1).any(axis=-1)
print(f'{duplicates2=}')
# this can be used as a mask on x to get the rows which are in z
print(f'{x[duplicates2]=}')