# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:48:09 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

xmin = -10
xmax = +10
nn   = 100
aa   = 2.0
bb   = 0.0

# original data
xx = np.linspace(xmin,xmax,nn)
noise = np.random.normal(0.0,1.0,size=(nn,))
yy = aa*xx + bb + noise
plt.scatter(xx,yy)


origdata = np.vstack((xx.reshape(1,-1),yy.reshape(1,-1)))

sigma = np.zeros((2,2),dtype='float64')

for ii in range(nn):
    sigma += np.outer(origdata[:,ii],origdata[:,ii])
    #print(sigma)
    
sigma = (1.0/nn)*sigma

UU,SS,VV = np.linalg.svd(sigma)

# project data
newdata = UU.T@origdata

plt.scatter(newdata[0,:],newdata[1,:]) 

# lower dimensional representation
Ulow = UU[:,0:1]
lowdata = Ulow.T@origdata

plt.scatter(lowdata[0,:],np.zeros((nn,),dtype='float64'))

# plot principal directions
# these are the rows of UU.T
# plot x = pt + x_min
#      y = qt + y_min
# p = UU.T[0,0] 
# q = UU.T[0,1]
pp = UU.T[0,0]
qq = UU.T[0,1]
tmax = (xmax-xmin)/pp

tt     = np.linspace(0.0,tmax,nn)
# this is a line parallel to the first principal direction
prinxx = pp*tt+xmin
prinyy = qq*tt+yy[0]

plt.plot(prinxx,prinyy,'r-')
plt.legend(['principal direction','original data','transformed data','low dim'])

 