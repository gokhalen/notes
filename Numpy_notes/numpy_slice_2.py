# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:06:04 2020

@author: Nachiket Gokhale
"""

import numpy as np;
import sys;

# B is a slice of A because we're using slice (2:4) notation
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b = a[2:4,2:4]
b +=100
print(f'{a=}')

print('-'*60)
# B is not a slice of A because we're referring to the elements of A directly
# a[2,2] returns a copy
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b = a[2,2]
b +=100
print(f'{a=}')
print('-'*60)

# if we refer using slice notation we'll get a view
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b = a[2:3,2:3]
b +=100
print(f'{a=}')
print('-'*60)

# we will get a copy for b
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b = a[[2],[2]]
b +=100
print(f'{a=}')
print('-'*60)
 
# we will still get a copy for b
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b = a[[2,3],[2,3]]
b +=100
print(f'{a=}')
print('-'*60)

# all dimensions have to be slices to be a view
aa = np.arange(16).reshape(4,4)
bb = aa[0:2,[0,1,2,3]]
bb += 100
print(f'{aa=}')
print(f'{bb=}')
print('-'*60)

# indexing on the left of the = is always a View
a = np.arange(16).reshape(4,4)
print(f'{a=}')
a[[2,3],[2,3]]  +=100
print(f'{a=}')
print('-'*60)

# ALWAYS a view on the left
aa = np.arange(16).reshape(4,4)
aa[0:2,[0,1,2,3]] +=100
print(f'{aa=}')
print('-'*60)


# so for we have seen cases where only one [] operator is used
# when there is only one operator, it is used to set values
# when multiple [] operators are used, the last one (rightmost) 
# is used to set values
# the previous ones are used to return either views of the original object
# if indexed using slice
# or copies of parts of the original object, if using general purpose notation


# Example at the end of
# https://scipy-cookbook.readthedocs.io/items/ViewsVsCopies.html

# a[islice,:] returns a slice 
# and as usual the succeeding [:,islice] modifies the view  i.e. original object
a = np.arange(12).reshape(3,4)
print(f'{a=}')
ifancy = [0,2]
islice = slice(0,3,2)
a[islice, :][:, ifancy] = 100
print(f'{a=}')
print('-'*60)

# a[ifancy,:] returns a copy because ifancy is NOT a slice
# the next [:,islice] modifies that copy, not the original a
a = np.arange(12).reshape(3,4)
print(f'{a=}')
ifancy = [0,2]
islice = slice(0,3,2)
a[ifancy, :][:, islice] = 100  # note that ifancy and islice are interchanged here
print(f'{a=}')
print('-'*60)

# what if we're taking [] on the right?
# as long as we're taking slices, we will get references or views
# e.g.

a = np.arange(10)
b = a[1:7][1:4:2]
b +=100
print(f'{a=}')
print(f'{b=}')
print('-'*60)

# whenever we use non-slice notation we will get a copy
a = np.arange(10)
b = a[1:7][[1,3]]
b +=100
print(f'{a=}')
print(f'{b=}')
print('-'*60)

# let's extend this to multi-d
# the [0:3,0:3] returns a slice
# the [[0,1],[0,1]] returns a copy
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b  = a[0:3,0:3][[0,1],[0,1]]
b +=100
print(f'{a=}') 
print(f'{b=}') 
print('-'*60)

