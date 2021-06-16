# -*- coding: utf-8 -*-

# In Beazley and Jones' Python Cookbook p.g. 600
# a callable is created using
# val = ((ctypes.c_double)*len(param))(*param)
# (ctypes.c_doublle*len(param)) creates the callable
# can then *param is passed to it
# we show how this might be done in python

# Note about __radd__
# These functions __radd__ are only called if the left operand
# does not support the corresponding operation using normal __add__ 
# (indicated by raising
# NotImplemented) 
# and the operands are of different types. For example,



import functools 
class createcallable:
    def __mul__(self,n):
        print('Callng __mul__')
        ff = functools.partial(self.ff,n=n)
        ff.__name__ = f'ff{n}'
        return ff
    @staticmethod
    def ff(*args,n):
        for _ in range(n):
            print(args[_])
cc = createcallable()
(cc*4)(*[1,2,3,4])