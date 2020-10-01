# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:44:54 2020

@author: aa
"""

import numpy as np

# dynamic axis indexing 
# https://stackoverflow.com/questions/31094641/dynamic-axis-indexing-of-numpy-ndarray

# given a 2D array "AA", and an axis (either 0,1)
# if axis is 0
#     return AA[0,:]*AA[1,:]*...*AA[nrow,:]
# if axis is 1
#     return AA[:,0]*AA[:,1]*...*AA[:,ncol]

# we can do this with an if statement 
# but a more elegant way is as follows

a = np.arange(9).reshape(3,3)

def ffprod(xx,ax):
    axdim  = xx.shape[ax]
    outarr = np.ones(axdim)
    for ii in range(axdim):
        sindex = [slice(None,None,None)]*xx.ndim
        sindex[ax] = ii
        sindex = tuple(sindex)
        outarr = outarr*xx[sindex]
    return outarr


print(ffprod(a,1))
