# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:31:02 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

aamin = np.asarray([5.0,5.0]) # the location of the minimum
bbecc = np.asarray([16.0,1.0]) # eccentricity of the ellipse
xmin = aamin[0]-10
xmax = aamin[0]+10 
ymin = aamin[1]-10
ymax = aamin[1]+10
nn   =  32

xvec = np.linspace(xmin,xmax,nn)
yvec = np.linspace(ymin,ymax,nn)

xx,yy = np.meshgrid(xvec,yvec)

alpha  = 0.1 # learning rate for steepest descent
xstart = np.asarray([xmax-1.0,ymax-1.0]) # initial point
niter  = 128 # number of iterations for steepest descent

def fobj(xx,yy,aa,bb):
    # objective function
    first  = ((xx-aa[0])**2)/bb[0]
    second = ((yy-aa[1])**2)/bb[1]
    return first + second

def fgrad(xx,aa,bb):
    return 2*(xx-aa)/bb

# HH is the hessian
HH = np.asarray([[2.0/bbecc[0],0],[0,2.0/bbecc[1]]])    

def plotiterates(xitertes,ax,clr='r'):
    nn = len(xiterates)
    for ii in range(nn-1):
        xstart = xiterates[ii]
        xend   = xiterates[ii+1]
        xx_ = xstart[0],xend[0]
        yy_ = xstart[1],xend[1]
        ax.plot(xstart[0],xstart[1],clr+'+')
        ax.plot(xx_,yy_,clr+'-')        

ff = fobj(xx,yy,aamin,bbecc)

fig = plt.figure()
ax = fig.gca()
ax.set_aspect('equal')
plt.contourf(xx,yy,ff)

# do steepest descent
# the step-size in steepest descent is based on a quadratic approximation
# in a particular direction (the gradient)!
xcurr     = xstart
xiterates = []
for iiter in range(0,niter):
    xiterates.append(xcurr)
    gg    = fgrad(xcurr,aamin,bbecc)
    alpha = gg@gg/(gg@HH@gg)
    xcurr = xcurr - alpha*gg

xiterates = np.asarray(xiterates)
plotiterates(xiterates,ax,'r')

# do newton
# Newton is based on quadratic-approximation in all-directions 
xcurr     = xstart
xiterates = []    
xiterates.append(xcurr)
xnew      = xstart - np.linalg.inv(HH)@fgrad(xcurr,aamin,bbecc)
xiterates.append(xnew)
xiterates = np.asarray(xiterates)
plotiterates(xiterates,ax,'b')

# do gradient descent with constant learning rate
xcurr = xstart 
xiterates = []
for iiter in range(0,niter):
    xiterates.append(xcurr)
    gg = fgrad(xcurr,aamin,bbecc)
    xcurr = xcurr - 0.16*gg

xiterates = np.asarray(xiterates)
plotiterates(xiterates,ax,'y')
