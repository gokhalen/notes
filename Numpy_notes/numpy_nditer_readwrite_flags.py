# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:57:54 2020

@author: Nachiket Gokhale
"""

import numpy as np
 
a = np.arange(24).reshape(2,3,4)
b = np.array(0)

# the 'readonly' seems to be a flag for a
# the 'readwrite' seems to be a flag for b
# more precisely, whatever is in the first list is a flag for first operand
# and whatever is in the second list is a flag for the second operand
with np.nditer([a,b], flags=['reduce_ok'],
               op_flags=[['readonly'],['readwrite']]) as it:
    for x,y in it:
        y[...] += x

print(b)