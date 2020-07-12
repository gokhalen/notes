# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:22:55 2020

@author: Gokhale
"""

# the * operator in numpy is elementwise 
# use the dot method or the @ operator for matrix products
# what happens when we try to take * products when array sizes don't match?
# answer: broadcasting!
# other elementwise operations, +,-,/ are also broadcast
# https://numpy.org/devdocs/user/basics.broadcasting.html#basics-broadcasting
# two dimensions are compatible when: 1) they are equal
#                                     2) one of them is 1
# also
# https://numpy.org/devdocs/user/quickstart.html#broadcasting-rules
import numpy as np
import itertools
import sys

# Case 1
a = np.arange(1,7).reshape(3,2)
b = np.arange(1,3).reshape(2)
c = a*b
# a and b do not have the same dimensions. So how is a*b defined?
# step 1: arrange the arrays so that dimensions are right justified
#         i.e. a.shape =   (3,2)
#         b.shape      =   (  2) 
# step 2: add a 'fake' first dimension to b to make it two dimensional
#         b.shape = (1,2)
#         since we are not increasing the number of elements 
b=b.reshape(1,2)
# step 3: expand the first dimension to 3
#         the entries (0,1), (0,2) in b are already defined
#         we define the entries (i,1) and (i,2) to be equal to (0,1) and (0,2)
#         for i > 0
#         to make things simple we can define a array d to take the place 
#         of expanded b
d = np.zeros(6).reshape(3,2)
for i,j in itertools.product(range(3),range(2)):
        d[i][j] = b[0][j]

e = a*d
#print('c=\n',c)
#print('e=\n',e)
#print('norm(c-e)=',np.linalg.norm(c-e))        
#print('-'*50)

c = a+b
e = a+d

#print('c=\n',c)
#print('e=\n',e)
#print('norm(c-e)=',np.linalg.norm(c-e))        
#print('-'*50)

#sys.exit()


# take a more general case
a = np.arange(48).reshape(8,1,6,1)
b = np.arange(35).reshape(7,1,5)
c = a*b

# as before, we right justify the matrices
# a.shape = (8,1,6,1)
# b.shape = (  7,1,5)
# add a dummy dimension to b
b=b.reshape(1,7,1,5)
# now that the number of dimensions are the same
# a.shape = (8,1,6,1)
# b.shape = (1,7,1,5)  
# we need to expand a and b 

# we define two expanded arrays
a_ex = np.zeros(8*7*6*5).reshape(8,7,6,5)
b_ex = np.zeros(8*7*6*5).reshape(8,7,6,5)


# using the power of numpy,the previous expansion algorithm can be written as 
a_ex[:,:,:,:] = a[:,0:1,:,0:1]
b_ex[:,:,:,:] = b[0:1,:,0:1,:]
# using a[:,0,:,0] will not work
# this itself is also referred to as broadcasting
# one can change 0:1 to ,0:2, 0:3 infact 0:n ,n>=1 because only one element 
# exists in that range 

a_ex_manual =  np.zeros(8*7*6*5).reshape(8,7,6,5)
b_ex_manual =  np.zeros(8*7*6*5).reshape(8,7,6,5)

# nested for loops can be simplified using itertools
for i,j,k,l in itertools.product(range(8),range(7),range(6),range(5)):
    a_ex_manual[i,j,k,l]=a[i][0][k][0]
    b_ex_manual[i,j,k,l]=b[0][j][0][l]
            
print('norm(a_ex - a_ex_manual) =',np.linalg.norm(a_ex - a_ex_manual))
print('norm(b_ex - b_ex_manual) =',np.linalg.norm(b_ex - b_ex_manual))

c_check = a_ex*b_ex

print('norm(c-c_check) =',np.linalg.norm(c-c_check))

# check 2 - explicitly perform the elementwise product
# the dot product is over common dimensions only
c_check_2 = np.zeros(8*7*6*5).reshape(8,7,6,5)
for i,j,k,l in itertools.product(range(8),range(7),range(6),range(5)):
    c_check_2[i,j,k,l]=a_ex[i,j,k,l]*b_ex[i,j,k,l]
    
print('norm(c-c_check_2) =',np.linalg.norm(c-c_check_2))
    