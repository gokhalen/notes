# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:30:53 2020

@author: aa
"""

# https://stackoverflow.com/questions/64166182/compare-numpy-arrays-of-different-shapes

import numpy as np
# A commong problem on SO is to find all pairs of differences.
aa = np.asarray([1,2,3]);
bb = np.asarray([4,7,1,5]);

# reshape aa to (3,1)
# reshape bb to (1,4)

aa2 = aa[:,np.newaxis]
bb2 = bb[np.newaxis,:]

# now due to broadcasting rules aa's shape changes from (3,1) to (3,4)
# with the property aa2[i,j] = aa2[i,0] = aa[i]  j>0
# now due to broadcasting rules bb's shape changes from (1,4) to (3,4)
# with the property bb2[i,j] = bb2[0,j] = bb2[j] i>0
# so now let cc = aa2 - bb2. therefore,
# cc[i,j] =  aa2[i,j] - bb2[i,j] = aa2[i,0] - bb2[0,j] == aa[i] - bb[j] 
# let's check

cc = aa2 - bb2;

print(f'{cc[1,2]=}')
print(f'{aa[1]-bb[2]=}')
print('-'*60)

aa  = np.arange(16).reshape(4,4)
bb  = np.arange(64,80).reshape(4,4)

# for higher dimensions, it works the same way
# if we're interested in all pairs of a[i,j] - b[k,l]
# reshape aa to (1,1,4,4) and bb to (4,4,1,1)
# aa2[i,j,k,l] = aa2[0,0,k,l] = aa[k,l]
# bb2[i,j,k,l] = bb2[i,j,0,0] = bb2[i,j]
# cc = aa2 - bb2 = aa2[i,j,k,l] - bb2[i,j,k,l] = aa2[k,l] - bb2[i,j]

aa2 = aa[np.newaxis,np.newaxis,:,:]
bb2 = bb[:,:,np.newaxis,np.newaxis]
cc  = aa2 - bb2;

print(f'{cc[1,2,0,3]=}')
print(f'{aa[0,3]-bb[1,2]=}')
print('-'*60)

# now back to the SO question that started it all
aa = np.arange(12).reshape(4,3);
bb = np.arange(12,15+12).reshape(5,3);
bb2 = bb[:,None]

# shape of bb2 is (5,1,3)
# when doing aa - bb2  
# aa first changes to (1,4,3) according to broadcasting rules
# bb2 is              (5,1,3) 
# Then, aa by broadcasting rules becomes (5,4,3)
# And,  bb by broadcasting rules becomes (5,4,3)

cc = aa == bb2 
# the above expression evaluates to 
# cc[i,j,k] = aa[i,j,k] == bb2[i,j,k]
#           = aa[0,j,k] == bb2[i,0,k]
#           = aa[j,k] == bb[i,k]
# I'm not being very precise with notation here
# so if we want to compare (see all entries are equal) the jth row vector from aa
# and the ith row vector of bb
# do np.all(c[i,j,:])


      

