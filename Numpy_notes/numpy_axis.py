# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:12:32 2020

@author: Gokhale
"""

import numpy as np
a = np.arange(12).reshape(2,6)
print('a=',a)
print('sum over axis 0=',a.sum(axis=0))
print('sum over axis 1=',a.sum(axis=1))
# pretty clear that axis=0 is on the left
# and axis=1 is on the right