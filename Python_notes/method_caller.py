# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:56:37 2020

@author: aa
"""

from operator import methodcaller

def fsquare(xx):
    return xx*xx

def fasis(xx):
    return xx


# we are calling multiple functions in the list [fsquare, fasis]
# on the same data '11'
*ans,=map(methodcaller('__call__',11),[fsquare,fasis])

print(ans)