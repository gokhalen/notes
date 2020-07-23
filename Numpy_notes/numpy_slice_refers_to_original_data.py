# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:52:31 2020

@author: Nachiket Gokhale
"""

import numpy as np
a=np.array([1]*10)
print(f'{a=}')

# b is a slice of a. In Numpy b points to the elements of a
b=a[1:5]
# the +1 operator modifies in place and NOT equivalent to b=b+1
b+=1
#b=b+1

print(f'{b=}')
print(f'{a=}')
print('-'*40)

# works for strided slices as well
a=np.array([1]*10)
print(f'{a=}')
b=a[::2]
b+=np.array([1,2,3,4,5])

print(f'{b=}')
print(f'{a=}')
print('-'*40)

# does it work for array-indexing? Apparently not. 
# it seems a little inconsistent but it is not. If you take a slice, 
# then you get a reference. Otherwise a new object is created and b
# points to it
a   = np.array(range(10))
idx = [1,3,9]
b=a[idx]
print(f'{b=}')
b+=1
print(f'{a=}')
print(f'{b=}')
print('-'*40)

# does it work for matrices? Yes!
a = np.arange(16).reshape(4,4)
print(f'{a=}')
b = a[2:4,2:4]
b +=10
print(f'{a=}')