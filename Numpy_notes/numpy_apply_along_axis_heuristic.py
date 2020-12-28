# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:49:56 2020

@author: aa
"""
import numpy as np
import sys

# 2D example
print('Simple 2D example')
aa = np.arange(2*3).reshape(2,3)
def ff(xx):
    print(f'calling ff {xx=}')
    return np.asarray([xx[0] +1,xx[1]+2,xx[2]+3])
output=np.apply_along_axis(ff,1,aa)

# take the three 1D arrays
# aa[:,0] => [0,3]
# aa[:,1] => [1,4]
# aa[:,2] => [2,5]
# make the vectors by taking the first element in the vertical direction
# [0,1,2]
# [3,4,5]
# and apply ff to them returning 
# [1,3,5]
# [4,6,8]
print('-'*60)

sys.exit()

# now for 3D
print('3D example')
aa = np.arange(2*3).reshape(2,3)
bb = np.zeros((2,3,4))
bb[:,:,0] = aa
bb[:,:,1] = aa
bb[:,:,2] = aa
bb[:,:,3] = aa
def ff(xx):
    print(f'calling ff {xx=}')
    return np.asarray([xx[0] +1,xx[1]+2,xx[2]+3,xx[3]+4])
output=np.apply_along_axis(ff,2,bb)

# numpy flattens bb[:,:,0],bb[:,:,1] and bb[:,:,2],bb[:,:,3]
# b0f = bb[:,:,0].ravel() = [0. 1. 2. 3. 4. 5.]
# b1f = bb[:,:,1].ravel() = [0. 1. 2. 3. 4. 5.]
# b2f = bb[:,:,2].ravel() = [0. 1. 2. 3. 4. 5.]
# b3f = bb[:,:,3].ravel() = [0. 1. 2. 3. 4. 5.]
# b0f,b1f,b2f,b3f have 2*3=6 elements each
# so we can make the following 6 vectors 
# v_i = [b0f[i] b1f[i] b2[i] b3[i]] ...i=0 to 5
# the function ff is applied to these v_i
# in the above case, 
# v_0 = [0,0,0,0]
# v_1 = [1,1,1,1]
# v_2 = [2,2,2,2]
# v_3 = [3,3,3,3]
# v_4 = [4,4,4,4]
# v_5 = [5,5,5,5] 
# assume that ff returns a N dimensional vector
# then the dimension of "output" is (2,3,N)
# Basically we have 6 vectors of dimension N
# these can be reshaped to (2,3,N)
# e.g. if N=4 as in abolve example, the output is 
# [1,2,3,4]
# [2,3,4,5]
# [3,4,5,6]
# [4,5,6,7]
# [5,6,7,8]
# [6,7,8,9]
# take each of these vertical vectors and reshape them into 
# (2,3) matrices and store those matrices sequentially in the 4th dimension
# i.e. 
# [1,2,3,4,5,6].reshape(2,3) = output[:,:,0]
# [2,3,4,5,6,7].reshape(2,3) = output[:,:,0]
# [3,4,5,6,7,8].reshape(2,3) = output[:,:,0]
# [4,5,6,7,8,9].reshape(2,3) = output[:,:,0]
print('-'*60)

print('3D Scalar return example')

# what if ff returns a scalar?
# we will have only one vector of dimension (2*3)
# this can be reshaped into shape (2,3)
# and that will be the shape of the output
aa = np.arange(2*3).reshape(2,3)
bb = np.zeros((2,3,4))
bb[:,:,0] = aa
bb[:,:,1] = aa
bb[:,:,2] = aa
bb[:,:,3] = aa
def ff(xx):
    print(f'calling ff {xx=}')
    return np.linalg.norm(xx)
output=np.apply_along_axis(ff,2,bb)
print('-'*60)

print('2D 2D-array return example')
# what if ff returns a 2D-array?
aa = np.arange(2*3).reshape(2,3)
def ff(xx):
    print(f'calling ff {xx=}')
    return np.outer(xx,xx)
output=np.apply_along_axis(ff,1,aa)

# As in the 2D case above the 1D vectors 
# are [0,1,2] and [3,4,5]
# the outer products are 
# array([[0, 0, 0],
#       [0, 1, 2],
#       [0, 2, 4]])
# 
# array([[ 9, 12, 15],
#       [12, 16, 20],
#       [15, 20, 25]])
# these arrays are stored in output[0,:,:]
# and output[1,:,:] respectively
# in other words the shape of "output" is expanded

print('-'*60)

# what about 3D arrays where ff returns a 2D array
aa = np.arange(2*3).reshape(2,3)
bb = np.zeros((2,3,4))
bb[:,:,0] = aa
bb[:,:,1] = aa
bb[:,:,2] = aa
bb[:,:,3] = aa
def ff(xx):
    print(f'calling ff {xx=}')
    return np.outer(xx,xx)
output=np.apply_along_axis(ff,2,bb)

# as before, the vectors on which ff operates are
# v_0 = [0,0,0,0]
# v_1 = [1,1,1,1]
# v_2 = [2,2,2,2]
# v_3 = [3,3,3,3]
# v_4 = [4,4,4,4]
# v_5 = [5,5,5,5] 
# cooresponding to each of these six vectors, ff computes a 2D array
# so, a higher dimensional object is created
# output[0,0,:,:] yields ff(v_0)
# output[0,1,:,:] yields ff(v_1)
# output[0,2,:,:] yields ff(v_2)
# output[1,0,:,:] yields ff(v_3)
# output[1,1,:,:] yields ff(v_4)
# output[1,2,:,:] yields ff(v_5)

print('-'*60)
