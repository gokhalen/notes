# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:46:47 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

# parameters of the 2D Gaussian
mu      = np.asarray([0.0,0.0])
cov_mat = np.asarray([[1,0],[0,1]]) 
nn      = 1024*4

xx = np.random.multivariate_normal(mu,cov_mat,size=(nn,))

plt.scatter(xx[:,0],xx[:,1])
plt.title('Covariance is identity')

plt.figure()
cov_mat = np.asarray([[8,0],[0,1]])
xx = np.random.multivariate_normal(mu,cov_mat,size=(nn,))
plt.scatter(xx[:,0],xx[:,1])
plt.title('More variance in x1 than x2')
ax = plt.gca()
ax.set_aspect('equal')


plt.figure()
# We want (1,1) and (-1,1) to be the principal directions
PP = np.asarray([[1,-1],[1,1]])/np.sqrt(2.0)
SS = np.asarray([[8,0],[0,1]])
cov_mat = PP@SS@PP.T
xx = np.random.multivariate_normal(mu,cov_mat,size=(nn,))
plt.scatter(xx[:,0],xx[:,1])
plt.title('Rotated')
ax = plt.gca()
ax.set_aspect('equal')
