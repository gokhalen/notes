# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:19:24 2022

@author: User
"""

import numpy as np
from scipy.optimize import minimize,LinearConstraint
import matplotlib.pyplot as plt

# number of positive and negative examples
npos = 64
nneg = 64
ntotal  = npos + nneg

# true separating hyperplane
# aa*x + bb*y + cc = 0
aa  = 4
bb  = 2  # assume bb is not zero
cc  = 1

# limits 
xmin,xmax = -10,10
half_width = 5

def generate_examples(xmin,xmax,ymin,ymax,nn,aa,bb,cc,half_width,which_class):
    # generate negative points
    px = np.random.uniform(low=xmin,high=xmax,size=(nn,))
    py = np.zeros_like(px)
    
    
    for idx_,px_ in enumerate(px):
        ylower = (-aa*px_ - cc - half_width)/bb
        yupper = (-aa*px_ - cc + half_width)/bb
        if which_class == 'positive':
            py[idx_] = np.random.uniform(low=yupper,high=ymax,size=(1,))[0]
        if which_class =='negative':
            py[idx_] = np.random.uniform(low=ymin,high=ylower,size=(1,))[0]
        
    
    return px,py
    

def obj_func(xx):
    # compute 0.5*|x|^2
    
    return 0.5*(xx[0]*xx[0] + xx[1]*xx[1])

def gradient(xx):
    
    gg = np.zeros_like(xx)
    gg[0] = xx[0]
    gg[1] = xx[1]
    
    return gg


fig = plt.figure(figsize=(8,8))
ax  = fig.gca()
ax.set_aspect('equal')

xx_true_hyper         = np.linspace(xmin,xmax,1024)
yy_true_hyper         = (-aa*xx_true_hyper -cc)/bb
# lower and upper boundaries of the "street"
yy_lower_true_hyper   = (-aa*xx_true_hyper - cc - half_width)/bb
yy_upper_true_hyper   = (-aa*xx_true_hyper - cc + half_width)/bb


# get y_limits note - they are for the upper and lower boundaries of the street
ymin,ymax = np.min(yy_lower_true_hyper),np.max(yy_upper_true_hyper)

# plot bounding box
plt.plot([xmin,xmax,xmax,xmin,xmin],[ymin,ymin,ymax,ymax,ymin],color='k')

# plot true hyperplane
plt.plot(xx_true_hyper,yy_true_hyper,color='k',linewidth=2,label='true hyperplane')

# plot lower "street"
plt.plot(xx_true_hyper,yy_lower_true_hyper,color='b',
         linewidth=2,linestyle='--',
         label='true lower boundary')

# plot upper "street"
plt.plot(xx_true_hyper,yy_upper_true_hyper,color='b',
         linewidth=2,linestyle='--',
         label='true upper boundary')

plt.legend(loc='upper right',bbox_to_anchor=(1.6,1.0))

# generate and plot positive and negative examples
pposx,pposy = generate_examples(xmin,xmax,ymin,ymax,npos,aa,bb,cc,half_width,'positive')
pnegx,pnegy = generate_examples(xmin,xmax,ymin,ymax,npos,aa,bb,cc,half_width,'negative') 

# make sure there are points on the half_width lines OPPOSITE to each other
# this is the only way that the calculated hyperplane will match
# with the line given by aa*x + bb*y + cc = 0
# the central line makes an angle theta = tan^-1 (a/b) with the negative x axis
# if we choose a point xx_special on the central line
# and drop perpendiculars to the sidelines
# then the difference in x-coordinate of central point the new points is
# (half_width/bb)*np.cos(theta)*np.sin(theta)
# the whole probelem is that the variable half_width is not the true half width
# the true half width is (half_width/bb)*np.cos(theta)

xx_special = (xmax+xmin)/2.0 + 3.0
theta      = np.arctan(aa/bb)
delta_x    = (half_width/bb)*np.cos(theta)*np.sin(theta)

pnegx[-1]  = xx_special-delta_x
pnegy[-1]  = (-aa*pnegx[-1] - cc - half_width)/bb
pposx[-1]  = xx_special+delta_x
pposy[-1]  = (-aa*pposx[-1] - cc + half_width)/bb

plt.plot(pposx,pposy,'r+')
plt.plot(pnegx,pnegy,'gx')

# draw supports
plt.plot([pposx[-1]],[pposy[-1]],'ro',linewidth=2)
plt.plot([pnegx[-1]],[pnegy[-1]],'go',linewidth=2)


# generate constraint matrix
# ((x^i)^T + b)t_i >= 1   t_i is a sign function
constraint_matrix = np.zeros(dtype='float64',shape=(ntotal,3))
lower_constraint  = np.zeros(dtype='float64',shape=(ntotal,))
upper_constraint  = np.zeros(dtype='float64',shape=(ntotal,))

lower_constraint[:] = 1
upper_constraint[:] = np.inf

for idx_ in range(nneg):
    constraint_matrix[idx_][0] = -pnegx[idx_]
    constraint_matrix[idx_][1] = -pnegy[idx_]
    constraint_matrix[idx_][2] = -1
    
for idx_ in range(npos):
    constraint_matrix[idx_ + nneg][0] = pposx[idx_]
    constraint_matrix[idx_ + nneg][1] = pposy[idx_]
    constraint_matrix[idx_ + nneg][2] = 1
    
linear_constraint = LinearConstraint(constraint_matrix,lower_constraint,upper_constraint)
    
    
x0  = np.asarray([7,3.1,2])
res = minimize(obj_func,x0,method='trust-constr',
               jac=gradient,constraints=[linear_constraint],
               tol=1e-16
               )

acomp = res['x'][0]
bcomp = res['x'][1]
ccomp = res['x'][2]

print('a= ',acomp,'b= ',bcomp,' c= ',ccomp)
print('a/c=',acomp/ccomp,'b/c=',bcomp/ccomp)
    
yy_pred_hyper = (-acomp*xx_true_hyper -ccomp)/bcomp
plt.plot(xx_true_hyper,yy_pred_hyper,'r-')

# find closest point to the predicted hyperplane
#dpos = np.abs(acomp*pposx + bcomp*pposy + cc)/np.sqrt(acomp*acomp + bcomp*bcomp)
#idx_dpos_min = np.argmin(dpos)
#x_dpos_min = pposx[idx_dpos_min]
#y_dpos_min = pposy[idx_dpos_min]
#
#plt.plot([x_dpos_min],[y_dpos_min],marker='o',color='crimson')
