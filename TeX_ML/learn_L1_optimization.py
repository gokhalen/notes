# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:38:49 2021

@author: User
"""

# L1 norm optimization

import numpy as np
import matplotlib.pyplot as plt

nn       = 1024
nnapprox = 32

aa = 1.0 # Goodfellows w_i^*
alpha = 0.1
xmin = aa-10
xmax = aa+10


def ffL1(xx,aa=aa,alpha=alpha):
    return 0.5*(xx-aa)*(xx-aa) + alpha*np.abs(xx)

# minimum - Goodfellow pg 235
xopt_ = np.abs(aa) -(alpha/1.0) 
xopt  = np.sign(aa)*np.maximum(xopt_,0)
yopt  = ffL1(xopt)

xx = np.linspace(xmin,xmax,nn)
yy = ffL1(xx)
yyquad = ffL1(xx,alpha=0.0)

plt.plot(xx,yy)
plt.plot(xx,yyquad)
plt.plot(xopt,yopt,'r+',markersize=16)
plt.legend(['Objective','Quadratic','Minimum'])