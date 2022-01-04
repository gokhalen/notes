# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 12:58:47 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

def project(pt,nn):
    # pt is 1-d array of length 2
    # nn is the unit vector defining the direction of projection
    proj = np.zeros(pt.shape[0],dtype='float64')
    for ii,pt_ in enumerate(pt):
        proj[ii] = np.dot(pt_,nn)
    return proj

nn   = 128
ndim = 2

# mu must be zero - because we are not subtracting means
mu     = [10.0,10.0]
eigval = [[1.0,0],[0,16.0]]
# construct a cov matrix with specified eigenvectors
theta  = (np.pi/180)*23

# number of rotated axes 
ntheta = 361
dtheta = 1
theta_array    = np.linspace(0.0,180,ntheta)


variance_array = np.zeros(shape=(ntheta,),dtype='float64') 

Q      = [
          [np.sin(theta), -np.cos(theta)],
          [np.cos(theta), np.sin(theta)]
         ]
mu     = np.asarray(mu)
eigval = np.asarray(eigval)
Q      = np.asarray(Q)
cov    = Q.T@eigval@Q


pts = np.random.multivariate_normal(mu,cov,nn)
# shift points to their mean
xmean,ymean = np.mean(pts,axis=0)
pts[:,0]   -= xmean
pts[:,1]   -= ymean 

total_variance = np.std(pts[:,0])**2 + np.std(pts[:,1])**2


#  loop over theta_array and fill variance_array
for itheta,theta_ in enumerate(theta_array):
    theta_ = (np.pi/180)*theta_
    nn_     = [np.cos(theta_),np.sin(theta_)]
    nn_     = np.asarray(nn_)
    proj_   = project(pts,nn_)
    variance_array[itheta] = np.std(proj_)**2

theta_max_var = theta_array[np.argmax(variance_array)]
variance_max  = np.max(variance_array)
variance_fraction = variance_max/total_variance
print(f'Manual: total_variance is {total_variance} maximum variance {variance_max} \
      is at {theta_max_var} deg  fraction = {variance_fraction}')

# direction and value of variance by svd
# By Ng's method
cov_mat = pts.T@pts/nn
U,S,VT = np.linalg.svd(cov_mat)

svd_theta_max_var    = np.arctan(U[1,0]/U[0,0])*180/np.pi
svd_variance_frac    =  S[0]/(S[0]+S[1])
svd_maximum_variance =  S[0]
svd_total_variance   =  (S[0] + S[1])

print(f'SVD: total_variance is {svd_total_variance}, maximum variance {svd_maximum_variance} the maximum variance is at \
      {svd_theta_max_var} deg, fraction is {svd_variance_frac}')

fig = plt.figure()
ax = fig.gca()
plt.scatter(pts[:,0],pts[:,1],linewidth=0.1)
# 45 degree line for reference
plt.plot([1,5],[1,5],'r-')
ax.set_aspect('equal')

# Now we will create a random orthogonal matrix and use it for projection
random_sym_matrix = np.random.random(size=(ndim,ndim))
random_sym_matrix = random_sym_matrix@random_sym_matrix
Q,SQ,QT           = np.linalg.svd(random_sym_matrix) 

# take the first column of Q
# SVD by IISc Method - they take the SVD of data matrix
# not covariance
# suffix I indicates IISc

U_I,S_I,V_IT = np.linalg.svd(pts)
S_I2 = np.zeros((U_I.shape[1],V_IT.shape[0]),dtype='float64')
np.fill_diagonal(S_I2,S_I)

# comparing projections can suffer from the fact 
# the sign of each eigenvector can be flipped around
proj_iisc  = pts@(V_IT.T)
proj_iisc2 = U_I@S_I2
proj_ng    = ((U.T@pts.T)).T

norm_diff_proj_iisc_ng = np.linalg.norm(proj_iisc-proj_ng)

print('norm_diff_proj=',norm_diff_proj_iisc_ng)

