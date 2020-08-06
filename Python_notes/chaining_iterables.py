# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:15:01 2020

@author: aa
"""

import itertools,copy
from operator import methodcaller

itrrange=iter(range(10))

def fsquare(xx):
    return xx*xx

def fasis(xx):
    return xx

def fchain1(xx):
    # if we con't have these copies, then we end up iterating 
    # over the same iterator. if itrrange is just 'range',
    # instead of 'iter(range)' the copies are made implicitly
    xx1 = copy.deepcopy(xx)
    xx2 = copy.deepcopy(xx)
    return (map(fsquare,xx1),map(fasis,xx2))
#    return map(methodcaller('__call__',xx),[fsquare,fasis])
     


def fchain2(xx):
    return itertools.chain(*fchain1(xx))

s1 = sum(fchain2(itrrange))

print(s1)