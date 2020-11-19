# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:13:13 2020

@author: aa
"""

from scipy.optimize import minimize
from collections import namedtuple
import numpy as np

def history(func):
    def wrapper(x):
        wrapper.history.append(x)
        return func(x)
    wrapper.history = []
    return wrapper

@history
def ff(x):
    return (x[0]-1)**2 + (x[1]-2)**2


b0 = (0.0,10.0)
b1 = (0.0,20.0)
bnds=(b0,b1)

if __name__ == '__main__':
   x0 = np.asarray([0.1,1000])
   solution = minimize(ff,x0,method='L-BFGS-B',bounds=bnds)
   print(f'{ff.history=}')