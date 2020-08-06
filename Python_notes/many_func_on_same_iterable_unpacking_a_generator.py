# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:56:37 2020

@author: aa
"""

from operator import methodcaller

itr = iter(range(16))

def fsquare(xx):
    return xx*xx

def fasis(xx):
    return xx


def many_func_on_same_iterable(funcs,itr):
    
    while True:
        try:
            data = next(itr)
        except StopIteration as e:
            return
    
        yield tuple([ff(data) for ff in funcs])
    

# we are calling multiple functions in the list [fsquare, fasis]
# on the same data '11'
*ans,= many_func_on_same_iterable([fasis,fsquare],itr)

print(ans)