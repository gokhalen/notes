# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:24:21 2021

@author: User
"""

# approximating a higher-order function locally with quadratic
# locally the approximation is good but it gets worse as we move away

import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy.utilities.lambdify import lambdify

xmin =   -10
xmax =    10
nn   =  1024

x = sympy.Symbol('x')

# make an alias for a function
exp_    = sympy.functions.elementary.exponential.exp

# function with local minima
fhigher = (x-3)**2 + 100*exp_((-(x-2.5)**2)/5)
fder1   = sympy.diff(fhigher)
fder2   = sympy.diff(fder1)   

fhigher_lam  = lambdify(x,fhigher)
fder1_lam    = lambdify(x,fder1)
fder2_lam    = lambdify(x,fder2)


# quadratic approximation about a point aa
def fqapprox(xx,aa=1.0):
    # f(a+(x-a)) = f(a) + f'(a)(x-a) + 0.5*f''(a)(x-a)**2
    return fhigher_lam(aa) + fder1_lam(aa)*(xx-aa) + 0.5*fder2_lam(aa)*(xx-aa)**2


xx       = np.linspace(xmin,xmax,nn)
yyhigh   = fhigher_lam(xx)
yyapprox = fqapprox(xx,aa=-0.8)

plt.plot(xx,yyhigh,'b-')
plt.plot(xx,yyapprox,'r-')