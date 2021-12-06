# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:38:49 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

nn       = 1024
nnapprox = 32

xmin = -10
xmax = 10

def ff(xx):
    return 0.5*xx*xx

def ffapprox(xx,xxstar=2.0):
    '''
    taylor expansion about arbitrary point xxstar
    '''
    first  = 0.5*xxstar*xxstar
    second = xxstar*(xx-xxstar)
    third  = 0.5*((xx-xxstar)**2)
    
    return first+second+third
    

xx = np.linspace(xmin,xmax,nn)
yy = ff(xx)

xxapprox = np.linspace(xmin,xmax,nnapprox)
yyapprox = ffapprox(xxapprox)

plt.plot(xx,yy)
plt.plot(xxapprox,yyapprox,'rx')
plt.legend(['exact','approx'])