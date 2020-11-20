# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:31:31 2020

@author: aa
"""
# inspired by
# https://stackoverflow.com/questions/64921773/extend-1d-numpy-array-in-multiple-dimensions

import numpy as np

# tiling 1d array
# repeats 4 times along the first axis
aa = np.asarray([10,12,15])
AA = np.tile(aa,(4,))
print(f'{AA=}')
print('-'*80)

# repeats in a (2,2) pattern
AA = np.tile(aa,(2,2))
print(f'{AA=}')
print('-'*80)

# based on this we can do 
# look at the last 2 entries -- (2,3)
# it is going make a (2,3) pattern as before and is going to 
# stuff it into (0,:,:) , (1,:,:), (2,:,:)
# similarly for higher dimensions
AA = np.tile(aa,(3,2,3))
print(f'{AA=}')
print(f'{AA[2,:,:]=}')
print('-'*80)

# now np.tile is going to create an array of shape
# (3*1,10*1,15*1,20*1)
# AA has shape (i,j,k,l),  0<=i<=2, 0<=j<=9,0<=k<=14,0<=l<=19
# AA(i,j,k,l) is going to be mapped to AA(i,0,0,0)
# as hpaulj said, it 'np.repeat's along an axis
AA = np.tile(aa.reshape(3,1,1,1),(1,10,15,20))

# simple example
# AA has shape (12,1,1,1) 
# AA[i,0,0,0] = AA[i%3,0,0,0]
# same thing happens for other indices
AA = np.tile(aa.reshape(3,1,1,1),(4,1,1,1))

print(f'{AA[:,0,0,0]=}')
print('-'*80)

# when, the shape passed to repeat is less than the shape of the matrix, 
# as below, then, the shapes are right aligned
#          (4,4)
#            (2,)
# so the output matrix will have shape (4,8)
# bb[i,j] = aa[i,j%2]
# similarly for higher dimensions

aa = np.arange(16).reshape(4,4)
bb = np.tile(aa,(2,))
print(f'{bb=}')
print('-'*80)