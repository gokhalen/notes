# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:54:00 2021

@author: User
"""

import numpy as np

# try to learn XOR with a linear model
# goodfellow, equation 6.1

XX    = np.asarray([[1, 0,0],[1,0,1],[1,1,0],[1,1,1]])
train = np.asarray([0,1,1,0])

weights = np.linalg.inv(XX.T@XX)@(XX.T@train)