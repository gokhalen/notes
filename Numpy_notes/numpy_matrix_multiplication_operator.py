# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:24:28 2020

@author: aa
"""

import numpy as np

# MeTchaikovsky's answer
# https://stackoverflow.com/questions/64939849/element-wise-matrix-vector-product-with-numpy

# Let B be a matrix (3,3)
# We know we can do B@A  where A.shape = (3,) or (3,1) or (3,M)
# what happens when A is (10,3,11) ?


A = np.random.random((10,3,11))
B = np.random.random((3,3))
C = B@A

# shape of C is (10,3,11)
# basically @ does a multiply with the ten (3,11) matrices 
# and returns a (10,3,11) array

# similarly 
A = np.random.random((10,17,3,11))
B = np.random.random((3,3))
C = B@A

# Shape of C is (10,17,3,11)
# for the 170 matrices (10,17,:,:) the result is (3,11)
# and is stored along the third and 4th dimension