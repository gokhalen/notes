# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:56:02 2020

@author: Gokhale
"""
import numpy as np

# hsplit splits along the second axis
# also referred to as the horizontal axis
a = np.arange(16).reshape(4,4)
b = np.hsplit(a,2)
print(b)
print('-'*40)
# this will split a in two parts along the second dimension
a = a.reshape(2,2,4)
b1,b2 = np.hsplit(a,2)
# b1 is same as a[:,0:1,:] i.e. a has been divided along dimension 1
print(b1)
print(a[:,0:1,:])
print('-'*40)
# b2 is same as a[:,1:2,:] i.e. a has been divided along dimension 2
print(b2)
print(a[:,1:2,:])
print('-'*40)
