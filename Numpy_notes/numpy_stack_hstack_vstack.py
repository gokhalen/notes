# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:37:46 2020

@author: aa
"""

import numpy as np

# stacks in the horizontal direction
aa = np.arange(9).reshape(3,3)
bb = np.arange(9).reshape(3,3)*2
cc = np.hstack([aa,bb])

print(f'{cc=}')
print('-'*80)

# stacks in the vertical direction
cc = np.vstack([aa,bb])
print(f'{cc=}')
print('-'*80)

# np.stack is different from hstack and vstack
# it creates an object one dimensional higher
# so here, the 2D arrays aa and bb will be put into
# cc[0,:,:] and cc[1,:,:] respectively
# if we specify axis=1 they will be put into
# cc[:,0,:] and cc[:,1,:] respectively
# if we specify axis=-1 or axis=2 they will be put into 
# cc[:,:,0] and cc[:,:,1] respectively
cc = np.stack([aa,bb],axis=0)
print(f'{cc[0,:,:]=}')
print(f'{cc[1,:,:]=}')
print('-'*80)

