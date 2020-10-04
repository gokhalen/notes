# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 09:49:39 2020

@author: aa
"""
import numpy as np

# Summary: Python integers do not overflow
# Numpy overflows, because the underlying C overflows

nn = 8**5
ll = list(range(8**5));
ll = [ l*l  for l in ll]
ss = sum(ll)

print(f'Pure python sum {ss}')

aa = np.arange(nn)
aa = aa*aa
ss = np.sum(aa)
ss2 = sum(aa)

print(f'OVERFLOW: NP sum of NP array {ss2}')
print(f'OVERFLOW: Python sum of NP array {ss2}')