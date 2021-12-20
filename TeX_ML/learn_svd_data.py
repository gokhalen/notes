# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:44:30 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

# https://jeremykun.com/2016/04/18/singular-value-decomposition-part-1-perspectives-on-linear-algebra/

AA = [[2,5,3],
      [1,2,1],
      [4,1,1],
      [3,5,2],
      [5,3,1],
      [4,5,5],
      [2,4,2],
      [2,2,5]
      ]

AA = np.asarray(AA)
U,S,VT = np.linalg.svd(AA,full_matrices=True)
u1 = U[:,0]
v1 = VT.T[:,0]
s1 = S[0]

# Rank 1 approximation to A
AAr1 = s1*np.outer(u1,v1)
# Rank 1 approximation to A.T
AAr1T = s1*np.outer(v1,u1)

# we can think of representing a new person
# in the basis of Aisha Bob and Chandrika
new_p =  np.asarray([0.33,0.33,0.33])
# We can calculate the movie ratins of the  person
rating_new_p_full = AA@new_p
# rating calculated by a rank 1 appx
rating_new_p_r1   = AAr1@new_p
print(f'{rating_new_p_full=}')
print(f'{rating_new_p_r1=}')
print('-'*80)

# we can think of representing a new movie
# using the basis of the eight movies
# and we want to predict the ratings of $A,B,C$
new_m = np.random.random(size=(8,))
new_m = new_m/np.sum(new_m)

# ratings of A,B,C
rating_new_m    = AA.T@new_m
# rating using rank1 approximation
rating_new_m_r1 = AAr1T@new_m

print(f'{rating_new_m=}')
print(f'{rating_new_m_r1=}')
print('-'*80)

