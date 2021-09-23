# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:48:17 2021

@author: User
"""

# https://stackoverflow.com/questions/69298405/valueerror-in-numba-vectorize-for-accumulate/69298828#69298828

import numpy as np
import numba as nb
arr = np.arange(15).reshape((3,5))
@nb.vectorize([(nb.int64, nb.int64)])
def myadd(x, y):
  return x+y
print(myadd.accumulate(arr, axis=1).astype(int))