# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:49:32 2020

@author: Nachiket 

# https://stackoverflow.com/q/45473896/13560598

"""

import numpy as np
from scipy.sparse.linalg import *  # gets solvers
from scipy import sparse,linalg


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
# define element rhs vectors r1 and r2
row=[0,3]
col=[0,0]
data=[1,1]
tt=(data,(row,col))
r1=sparse.coo_matrix(tt,shape=(N,1))
rhs_global += r1

row=[0,7]
col=[0,0]
data=[1,1]
tt=(data,(row,col))
r2=sparse.coo_matrix(tt,shape=(N,1))
rhs_global += r2

print(rhs_global.todense())
print('-'*40)

# since we have assembled only two 'elements' the global matrix is singular
# add '1' to the global matrix to make it non-singular

row=list(range(N))
col=row
data=[ 1 for i in range(N)] # or alternatively data = [1]*N
tt=(data,(row,col))
kreg=sparse.coo_matrix(tt,shape=(N,N))

K_global +=kreg

rhs_global=rhs_global.reshape(N,1)
# x=scipy.sparse.linalg.spsolve(K_global,rhs_global)
# sparse solvers require dense right hand sides
x,exitCode=bicg(K_global,rhs_global.todense())
# for some reason the shape of the vector returned is (N,) i.e. a row vector
# make it a column vector
x=x.reshape(N,1)
print(f'{K_global.dot(x)=}')
boolvec = K_global.dot(x) == rhs_global
# everything is not true because of floating point comparisons
print(f'{boolvec=}')