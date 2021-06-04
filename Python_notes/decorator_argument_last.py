# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:53:05 2021

@author: aa
"""

from functools import partial

# Beazley and Jones, Python Cookbook. p.g.336

def attach_wrapper(obj, func=None):
    print(f'{obj=},{func=}')
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

# as per p.g. 341 in beazley jones the calling sequence for 
# decorators with arguments is 
# 
# func= attach_wrapper(obj=someting) (func)
#       ----------------------------
# the underlined is the first call to attach_wrapper
# since func is not defined, it is None
# the code goes to the first return and returns
# partial of attach_wrapper which accepts only once argument
# which is func
# this partial of attach_wrapper is called again

def host_func():
    print('Host function')


# obj is set to host_func and the last positional argument func is 
# the function/object being decorated. in this case, attached_func
@attach_wrapper(obj=host_func)
def attached_func():
    print('Attached func')

    

