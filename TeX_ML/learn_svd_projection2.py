# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 10:33:30 2022

@author: User
"""

import numpy as np

# dimension of space
nn = 2

# dimension of projection space
kk = 1

AA = np.random.random(size=(nn,nn))
U,S,VT = np.linalg.svd(AA,full_matrices=True)

xx = np.random.random(size=(nn,))

Uproj = np.zeros(shape=(nn,nn),dtype='float64')
Uproj[:,0:kk] = U[:,0:kk] 

xproj = Uproj.T@xx
print(f'{xproj=}')
xproj2 = Uproj.T@xproj
print(f'{xproj2=}')
