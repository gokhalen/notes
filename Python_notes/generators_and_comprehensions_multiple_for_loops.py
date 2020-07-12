# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:37:11 2020

@author: Gokhale
"""

# In Python 3.7+ dictionaries remember the order of items inserted
# j values take change rapidly indicating the second for is the inner loop
ll=['a','b','c']
mm=['d','e','f']
dd={ (ii,jj):(ii,jj) for ii in ll for jj in mm }

# similarly for generator expressions
gg=(f'{ii},{jj}' for ii in ll for jj in mm)

for _ in gg:
    print(_)
    
ar = [('four' if i % 4 == 0 else ('six' if i % 6 == 0 else i)) for i in range(1, n)]
print(ar)

def even_or_odd(ii):
    if ii % 2 == 0:
        return 'even'
    else:
        return 'odd

gg = ( even_or_odd(ii) for ii in range(10))
for _ in gg:
    print(_)
    