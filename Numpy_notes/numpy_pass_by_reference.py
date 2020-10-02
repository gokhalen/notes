# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:08:39 2020

@author: aa
"""

import numpy as np

# the following works as expected
# b is an alias for a
# when b in modified in place
# a gets modified too

aa=np.arange(9).reshape(3,3)
bb=np.zeros(9,dtype='int32').reshape(3,3)
cc=np.zeros(9,dtype='int32').reshape(3,3)
aa=bb;
bb+=100;

print(f'{aa=}')
print(f'{bb=}')
print('-'*60)

# in the following c[:,:] calls the setitem method of cc
# cc is NOT an alias for aa
# cc[:,:] calls the __setitem__ method of cc

aa=np.arange(9).reshape(3,3)
cc=np.zeros(9,dtype='int32').reshape(3,3)
cc[:,:] = aa
cc += 100
print(f'{aa=}')
print(f'{cc=}')
print('-'*60)



