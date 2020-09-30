# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:51:30 2020

@author: aa
"""



# https://stackoverflow.com/questions/64137179/numpy-get-values-at-indices-given-in-array-form

import numpy as np

my_array = np.array([[[1.1587323 , 1.75406635],
        [1.05464125, 1.29215026],
        [0.9784655 , 1.16957462]]]);

indices = np.array([[[0],
        [1],
        [0]]]);

# required output 
req_output = np.array([[[1.1587323], [1.29215026], [0.9784655]]])

# solution provided
take_output=np.take_along_axis(my_array, indices, axis=-1)

# axis = -1 refers to last axis, just as with indexing

# when we take along a given axes, we loop over the other axes
# the other axes here are the axes labeled 0 and 1
# the dimension/length of the axes we take along is defined as
# the dimension of the cooresponding axes in "indices"
# here we are taking along the axis labeled 2 

aa = np.zeros((1,3,1));
aa[0][0][0] = my_array[0][0][indices[0][0][0]];
aa[0][1][0] = my_array[0][1][indices[0][1][0]];
aa[0][2][0] = my_array[0][2][indices[0][2][0]];

# can check aa = req_output = take_output

# a further example
aa = np.zeros((1,3,2));
idx2=np.zeros((1,3,2),dtype='int32');
idx2[:,:,0] = indices[:,:,0]
idx2[:,:,1] = indices[:,:,0]

take_output=np.take_along_axis(my_array, idx2, axis=-1);
aa[0][0][0] = my_array[0][0][idx2[0][0][0]];
aa[0][1][0] = my_array[0][1][idx2[0][1][0]];
aa[0][2][0] = my_array[0][2][idx2[0][2][0]];
aa[0][0][1] = my_array[0][0][idx2[0][0][1]];
aa[0][1][1] = my_array[0][1][idx2[0][1][1]];
aa[0][2][1] = my_array[0][2][idx2[0][2][1]];


print(f'{aa=}')
print(f'{take_output=}')












