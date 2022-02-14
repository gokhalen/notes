# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:30:24 2022

@author: User
"""

# We plot the contour of a function
# in which the scales of the features are different

import numpy as np
import matplotlib.pyplot as plt

# number of data points
ndata = 1
nfeat = 2 
nrows = 128
ncols = 64

# features
xx = np.random.random(size=(ndata,2))

# make one feature different from the other
xx[:,0] = 10
xx[:,1] = 1

# yy = theta_0*x_0 + theta_1*x_1
ytrue = xx[:,0]*3 + xx[:,1]*2

theta0_ = np.linspace(0,10,ncols)
theta1_ = np.linspace(-10,10,nrows)

theta0,theta1 = np.meshgrid(theta0_,theta1_)
# loss function for various theta1,theta1
yloss = np.zeros_like(theta0)

for icols in range(ncols):
    for irows in range(nrows):
        ypred = np.zeros_like(ytrue)
        for idata in range(ndata):
            ypred[idata] = theta0[irows,icols]*xx[idata,0] \
                         + theta1[irows,icols]*xx[idata,1]  
                         
        yloss[irows,icols] = np.linalg.norm(ypred-ytrue)**2
        

yloss_true = ytrue - xx[:,0]*3 - xx[:,1]*2
        
plt.pcolormesh(theta0,theta1,yloss)
plt.colorbar()
plt.figure()
plt.contour(theta0,theta1,yloss,128)
plt.colorbar()


