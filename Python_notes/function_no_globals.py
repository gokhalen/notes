# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:39:46 2020

@author: aa
"""

import types

# https://stackoverflow.com/questions/31023060/disable-global-variable-lookup-in-python

a = 1
b = 2

# this will return 3, irrespective of the arguments
# it grabs a anb b from the global namespace 
def mysum(a0,b0):
    return a + b

c = mysum(11,13)
print(f'{c=}')

# creating a new function with the code of line and an empty dictionary 
# for globals
mysum2 = types.FunctionType(mysum.__code__, {})

# throws an error a is not defined
# c = mysum2(11,13)
# print(f'{c=}')

# we can make a decorator
def noglobals(func):
    ff = types.FunctionType(func.__code__, {},argdefs=func.__defaults__)
    return ff

@noglobals
def mysum3(a0,b0):
    return a + b

if __name__ =='__main__':
    a = 23
    b = 24
    # this prints 47
    c = mysum(11,12)
    print(f'{c=}')
    # this throws an error
    # c = mysum2(11,12)
    # this also throws an error
    c = mysum3(11,12)
