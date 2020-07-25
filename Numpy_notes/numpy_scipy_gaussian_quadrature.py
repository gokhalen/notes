# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:19:20 2020

@author: aa
"""


from scipy.special import roots_legendre

 
(p1d,w1d)=roots_legendre(3)
print(p1d,w1d)

# cache the weights 