# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 15:00:17 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt


xmin = -5
xmax =  5
nn   = 1024
hh   = (xmax-xmin)/nn


def fgauss(xx,mu=0,sigma=1):
    coeff = np.sqrt(1.0/(2*np.pi*sigma*sigma))
    power = -(1.0/(2.0*sigma*sigma))*(xx-mu)**2
    fg  = coeff*np.exp(power)
    return fg
    
    
xx  = np.linspace(xmin,xmax,nn)    
yy  = fgauss(xx)
yy1 = np.diff(yy)/hh
yy2 = np.diff(yy1)/(hh)
plt.plot(xx,yy)
plt.plot(xx[:-1],yy1)
plt.plot(xx[:-2],yy2)
plt.legend(['value','1st-der','2nd-der'])    