# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:12:32 2020

@author: Gokhale
"""

import numpy as np

# concatenate algorithm illustrated with 3 axis (3D) arrays
# given two arrays a[p_1][q][r],b[p_2][q][r]
# to concatenate along axis 1 we do
# axis 1 of the concatenated array is expanded to length p_1 + p_2
# the other axes must be compatible 
# i.e. equal in the num of elements they contain in each dimension
# for i in range(0,p_1 + p_2):
#   for j in range (0,q):
#       for k in range(0,r):
#           if (i < p_1):    
#             c[i][j][k] = a[i][j][k]
#           if (p_1 <= i < p_1 + p_2)
#             c[i][j][k] = b[i-p_1][j][k]
#
# similar code to concatenate along other axes, and multiple arrays and 
# other dimensional arrrays 

# hstack and vstack
# vstack concatenates along the first axis
# hstack concatenates along the second axis

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.vstack((a,b))
# vstack 
#print(repr(c))
c = np.hstack((a,b))
# hstack
#print(repr(c))
# row_stack
# row_stack is equivalent to vstack
# row_stack is an alias for vstack
# c = np.row_stack((a,b))
# print(repr(c))
# column_stack
# https://numpy.org/devdocs/user/quickstart.html
# the above page says that column_stack is equivalent to
# hstack only for 2D arrays. But I seem to get same results
# from hstack and column_stack for 3d arrays
# c = np.column_stack((a,b))
# print(repr(c))


#r_ and c_
a=np.arange(4).reshape(2,2)
b=np.arange(4,8).reshape(2,2)
# r_ is rowstack,vstack
c=np.r_[a,b]
#print(repr(c))
# c_ is colstack,hstack
c=np.c_[a,b]
#print(repr(c))
#when range literals (:) are used, the behavior is apparently different
#the following makes a 1D array
#c=np.r_[1:4,4,5,6:9]
#print(repr(c))
#the following makes a 2D array
#c=np.c_[1,2,3,4]
#print(repr(c))
#range literals have to be of equal size
#c=np.c_[1:4,4:7]
#print(repr(c))
