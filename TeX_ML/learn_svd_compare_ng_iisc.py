# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:28verbat:20 2022

@author: Nachiket Gokhale
"""

import numpy as np

mm = 4  # number of data points
nn = 5  # number of features
kk = 2  # number of columns to use for projection

# Andrew Ng's method

xx     = np.random.random(size=(mm,nn))
#x_mean = np.mean(xx,axis=1).reshape((mm,1))
x_mean = np.mean(xx,axis=0)
XX     = xx - x_mean

Sig_ng = (1.0/mm)*XX.T@XX


U_ng,S_ng,VT_ng = np.linalg.svd(Sig_ng)
S_ng = np.diag(S_ng)

proj_ng = U_ng[:,0:kk]

z_ng    = proj_ng.T@XX.T


# IISc 
# Last part of Matrix_Decompositions pdf
z_iisc = XX@VT_ng.T[:,0:kk]

print('z_ng and z_iisc are transposes of each other')
print('z_ng=',z_ng)
print('z_iisc=',z_iisc)

# the following lines are equivalent
# proj_ng.T@XX[0,:]
# XX[0,:]@VT_ng.T[:,0:kk]