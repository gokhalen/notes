# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:40:39 2020

@author: Gokhale
"""

import numpy as np
import itertools

a=np.zeros(16).reshape(4,4)
b=np.arange(1,17).reshape(4,4)
c=np.arange(1,5).reshape(4,1)
d=np.arange(1,5)

a_manual = np.zeros(16).reshape(4,4)

# Point 1 
a[:,:]=b[:,0:1]
# the above code does the following
for irow,jcol in itertools.product(range(4),range(4)):
      a_manual[irow,jcol] = b[irow,0]

#print('a=\n',a)
#print('a_manual=\n',a_manual)
#print('b=\n',b)

# Point 2
# the following code is __NOT__ equivalent to code in Point 1
a[:,:] = b[:,0]
# the right hand side is a vector i.e. it has only one dimension
# broadcasting will take place as follows
# right-justify (align) the shape
# a.shape      = (4,4) 
# b[:,0].shape = (  4)
# loop over excess dimensions, assign the common dimensions
for irow, jrow in itertools.product(range(4),repeat=2):
    a_manual[irow][jrow] = b[jrow,0]
    
#print('a=\n',a)
#print('a_manual=\n',a_manual)
#print('b=\n',b)


# Point 3
# in Point 1 and 2 there were selection operators on the left
# In the following code, there are no selection operators on the left
# Therefore, no broadcasting takes place
# d.shape = b[:,0:1].shape = (4,1).
# e.shape = b[:,0].shape   = (4,)
# Note: since a range '0:1' was specified in selecting the second dimension 
# of b, d has two dimensions/axes, even though there is exactly 
# one element between 0:1. Since a plain 0 was specified in the second dimension 
# of b, e has only one dimension. 
d = b[:,0:1]
e = b[:,0]
#print('d=\n',d)
#print('e=\n',e)

# Point 4 
# Overselection from a b(4,1) matrix
f = np.arange(1,5).reshape(4,1)
g = np.zeros(16).reshape(4,4)
# the following fails with an error 
# could not broadcast input array from shape (4,2) into shape (4,4)
# g[:,:] = b[:,0:2]
# but the following works
g[:,:] = f[:,0:2] 
# this is because 0:2 selects only one element in the second dimension
# from f.  f[:,0:2] then has shape (4,1) which can be broadcast into (4,4)
# the following also works because there is only one component between 0:5
g[:,:] = f[:,0:5] 

# also note
a[:,:] = 2
# yields a matrix with all twos. This is a special case
# in the following: b[:] means b[:,:] because dimensions left out are 
# defaulted to ':'
a[:,:] = b[:]