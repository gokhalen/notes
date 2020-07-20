# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:15:11 2020
@author: Nachiket Gokhale

Explanation of op_axes in 
https://numpy.org/devdocs/reference/arrays.nditer.html#reduction-iteration
is confusing

Basically, a value for op_axes like [1,2,0] tells the iterator to treat the 
0th axis of the array as axis 1, the 1st axis as  axis 2 and 3rd axis as axis 0 

"""
import numpy as np
a = np.arange(4).reshape(2,2)
a = np.array(a,order='C')

print(a)
print('-'*40)

# prints in c-order i.e. last index changes fastest
it = np.nditer(a,order='C')
for x in it:
    print(x)

print('-'*40)

# now we're telling it to treat axis 0 as 1 and axis 1 as 0
# when it normally loops over axis 0, it will loop over axis 1
# when it normally loops over axis 1, it will loop over axis 0
# effectively we're telling it to transpose it  
# if we have multiple objects, we can use None to set default ordering
# for that particular object
it = np.nditer(a,order='C',op_axes=[None])
for x in it:
    print(x)

