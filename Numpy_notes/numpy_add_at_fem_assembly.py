# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:49:32 2020

@author: Nachiket 

# https://stackoverflow.com/q/45473896/13560598

"""

import numpy as np
from scipy import sparse

x       = np.arange(8)
indices = np.array([1,5,7])
data    = np.array([11,12,13])

np.add.at(x,indices,data)

print(x)
print('-'*40)


idx = tuple([[0,4,1], [3,2,4]])
dW = np.zeros((5,6),int)
np.add.at(dW,idx,data)

print(dW)
print('-'*40)

# for assembly just create sparse matrices in each element and assemble them
# Let there be NN=8 global dofs
N=8 
K_global=sparse.coo_matrix(np.zeros(N*N).reshape(N,N))
# define two 2x2 element level matrices in global indices
# for k1 let the global indices be [ [(0,0) (0,3)], [(3,0), (3,3)]
# so the arrays are row=[0,0,3,3] and col=[0,3,0,3] and data=[2, -1, -1,2]
# 
row=[0,0,3,3]
col=[0,3,0,3]
data=[2,-1,-1,2]

tt=(data,(row,col))
k1=sparse.coo_matrix(tt,shape=(N,N))
K_global += k1
print(K_global.todense())
print('-'*40)

# define k2. let global indices be [ [(0,0) (0,7)], [ (7,0), (7,7)] ]
row=[0,0,7,7]
col=[0,7,0,7]
tt=(data,(row,col))
k2=sparse.coo_matrix(tt,shape=(N,N))
K_global +=k2

print(K_global.todense())
print('-'*40)

# now define a right hand side
rhs_global=sparse.coo_matrix(np.zeros(N).reshape(N,1))