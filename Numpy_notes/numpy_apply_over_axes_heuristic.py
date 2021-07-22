# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:40:56 2020

@author: aa
"""
import numpy as np,sys

# sum over axis zero is carried out
# extra dimension is added to compensate for loss of dim
a = np.arange(4)
output = np.apply_over_axes(np.sum,a,0)
print(f'{output=}')
print('-'*60)


a = np.arange(9).reshape(3,3)
output = np.apply_over_axes(np.sum,a,[0,1])
print(f'{output=}')
print('-'*60)

sys.exit()

# we sum over dimension 0, add an extra dimension 
# to compensate for loss of dimension
# then sum over dimension 1
# add a dimension to compensate for the loss of dim
a = np.arange(9).reshape(3,3)
def ff(xx,ax):
    print(f'Calling ff, {xx=},{ax=}')
    return np.sum(xx,ax)
output = np.apply_over_axes(ff,a,[0,1])
print(f'{output=}')
print('-'*60)

# since, dimensions are not being lost, nothing interesting happens
a = np.arange(9).reshape(3,3)
def ff(xx,ax):
    print(f'Calling ff, {xx=},{ax=}')
    return xx*xx
                  
output = np.apply_over_axes(ff,a,[0,1])
print(f'{output=}')
print('-'*60)




