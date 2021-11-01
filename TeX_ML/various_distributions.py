# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:11:03 2021

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

def fexp(xx,lam=1.0):
    indicator = (xx > 0).astype(int)
    return indicator*lam*np.exp(-lam*xx)

def flaplace(xx,mu=1.0,gamma=1.0):
    return (1.0/(2.0*gamma))*np.exp(-np.abs(xx-mu)/gamma)

xx  = np.linspace(xmin,xmax,nn)    
yy  = fgauss(xx)
yy1 = fexp(xx)
yy2 = flaplace(xx)
plt.plot(xx,yy)
plt.plot(xx,yy1)
plt.plot(xx,yy2)
