# -*- coding: utf-8 -*-

# GoodFellow, Deep Learning, section 4.5

import numpy as np
import matplotlib.pyplot as plt

nn = 4


niter = 600 # global iterations
nintern = 3000  # internal iterations
alphax = 1e-5 # learning rate
alphal =  1e-5


# We're trying to minimize  (0.5)*x'x 
# subject to 1-x'x <=0
# Withot the constraint the minimum is at x=0
# With contraint the minimum will be at the smallest x'x
# which satisfies the constraint


# initial guess 

xx = np.asarray([3]*nn)
# strangely even this guess produces [0.5,0.5,0.5,0.5]
# as an answer, even though it is already optimal
# xx = np.asarray([1,0,0,0])
lam = 1.0 # lam >0
gradxx  = []
gradll  = []
lamvals = []

for iiter in range(niter):
    
    for il in range(nintern):
        # Gradient ascent on lamda
        gl = (1-xx.T@xx)
        lam = lam + alphal*gl

    
    for ix in range(nintern):
        # gradient descent on x
        gx = xx + lam*(1-2*xx)
        xx = xx - alphax*gx
    
    gradxx.append(np.linalg.norm(gx))
    gradll.append(gl)
    lamvals.append(lam)
    #print(f'{xx=},{lam=},{gx=},{gl=}')
    #print('-'*80)


plt.figure()
plt.plot(range(niter),gradxx)
plt.title('gradxx')

plt.figure()
plt.plot(range(niter),gradll)
plt.title('gradll')

plt.figure()
plt.plot(range(niter),lamvals)
plt.title('lamvals')

print('normalized calculated xx =', xx/np.linalg.norm(xx))
print('calculated xx = ', xx)

