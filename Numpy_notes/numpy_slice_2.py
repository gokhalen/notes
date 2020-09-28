# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:06:04 2020

@author: Nachiket Gokhale
"""

import numpy as np;

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

# indexing on the left of the = is always a view
a = np.arange(16).reshape(4,4)
print(f'{a=}')
a[[2,3],[2,3]]  +=100
print(f'{a=}')
print('-'*60)

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

