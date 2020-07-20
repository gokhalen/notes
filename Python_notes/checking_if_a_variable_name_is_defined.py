# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:56:29 2020

@author: Gokhale
"""


try:
    x
except NameError as e:
    print(e)
    
try:
    x = x+1
except NameError as e:
    print(e)