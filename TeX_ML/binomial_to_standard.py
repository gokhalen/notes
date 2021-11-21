# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:49:48 2021

@author: User
"""



# shows that a binomial distribution (k successes and n-trials)
# can be approximated by a normal distribution
# as n is large and p = 0.5

# approximation is very good for nn=64 and just gets better from thereon

import numpy as np
import matplotlib.pyplot as plt
import scipy.special

nn = 64
pp = 0.5
qq = 1.0 - pp
mean  = nn*pp
sigma = np.sqrt(nn*pp*qq)

pbino = np.zeros((nn+1,),dtype='float64')
pnorm = np.zeros((nn+1,),dtype='float64')

xx = np.asarray(np.arange(0,nn+1))
factor = (1.0/sigma)*(1.0/np.sqrt(2.0*np.pi))

for kk in range(0,nn+1):
    pbino[kk-1] = scipy.special.comb(nn,kk)*(pp**kk)*(qq**(nn-kk))
    zz2 = ((kk-mean)/sigma)**2
    pnorm[kk-1] = factor*np.exp(-0.5*zz2)
    
plt.plot(xx,pbino,'b-')
plt.plot(xx,pnorm,'r+')
plt.legend(['prob binomial','prob normal approx'],loc='upper right')
print('sum of normal =',np.sum(pnorm))
print('sum of binomial =',np.sum(pbino))