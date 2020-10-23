# We will create functions that accept a 2D array
# Adds 1.0 to every element and then returns the sum
# of all elements in the array
# Tested on Python 3.8.5 and Numba 0.51.2
# Nachiket Gokhale gokhalen@gmail.com

# arrsum_py   - a pure python function (very slow)
# arrsum_njit - a JIT compiled function
# arrsym_cc   - a ahead of time compiled function

import numba as nb
import numpy as np
from numba.pycc import CC
from timerit import Timer  # a timing library
from collections import namedtuple

# the pure python function
def arrsum_py(nn,xx):
    arraysum = 0.0
    for i in range(nn):
        for j in range(nn):
            xx[i,j]  += 1.0
            arraysum += xx[i,j]
    return arraysum

# this is the JIT compiled version
# the function signature is specified (seems to make compilation faster)
# perhaps because the compiler does not need to generate code
# for all possible combinations of argument types
@nb.njit((nb.float64)(nb.int64,nb.float64[:,:]),fastmath=True)
def arrsum_njit(nn,xx):
    arraysum = 0.0
    for i in range(nn):
        for j in range(nn):
            xx[i,j]  += 1.0
            arraysum += xx[i,j]
    return arraysum



# this is our compiler used for ahead of time compilation
# 'arrsum_mod' is the module into which the precompiled
# function will be placed
cc = CC('arrsum_mod')
# this is the compiled version of the function
@cc.export('arrsum_cc',(nb.float64)(nb.int64,nb.float64[:,:]))
def arrsum_cc(nn,xx):
    arraysum = 0.0
    for i in range(nn):
        for j in range(nn):
            xx[i,j]  += 1.0
            arraysum += xx[i,j]
    return arraysum

# This produces: arrsum_mod.cpython-38-x86_64-linux-gnu.so
# from which we can import arrsum_cc
cc.compile()
    
if __name__ == '__main__':
    
    from arrsum_mod import arrsum_cc
    ttim = Timer('Sum Timer',verbose=0)
    nn   = 64
    xx   = np.zeros(nn*nn,dtype='float64').reshape(nn,nn)

    with ttim:
        arraysum = arrsum_py(nn,xx)
    print(f'Pure Python time = {ttim.elapsed:0.3f}s')

    xx   = np.zeros(nn*nn,dtype='float64').reshape(nn,nn)
    with ttim:
        arraysum = arrsum_njit(nn,xx)
    print(f'JIT time = {ttim.elapsed:0.3f}s')

    xx   = np.zeros(nn*nn,dtype='float64').reshape(nn,nn)
    with ttim:
        arraysum = arrsum_cc(nn,xx)
    print(f'Precompiled time = {ttim.elapsed:0.3f}s')

