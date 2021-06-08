# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:18:34 2021

@author: aa
"""

import types
from functools import wraps

class Profiled:
    def __init__(self,func):
        print('Calling init: func=',func)
        # see below for explanation
        # wraps is copying metadata from func to self (self is callable)
        wraps(func)(self)
        self.ncalls = 0
        
    def __call__(self,*args,**kwargs):
        print('Calling __call__')
        self.ncalls +=1
        return self.__wrapped__(*args,**kwargs)
    
    def __get__(self,instance,cls):
        print('Calling __get__')
        # self is Profiled object
        # instance is Spam object (in the example below)
        # cls is class Spam (in the example below)
        # much like descriptors we can get state of the 
        # object which encloses the decorated function into
        # the decorator through instance
        print(f'{self=},{instance=},{cls=}')
        if (instance is None):
            return self
        else:
            # I think here self is the callable which is bound to instance
            return types.MethodType(self,instance)

# as usual, this translates to 'add=Profiled(add)'
# add on the right is a function
# add on the left is a callable class        
@Profiled
def add(x,y):
    return x+y

# __get__ is not called in the three prints below
print(add(2,3))
print(add(4,5))
print(f'{add.ncalls=}')

class Spam:
 @Profiled
 def bar(self, x):
     print(self, x)
     
# __get__ gets called below
s = Spam()
s.bar(1)


'''
#binding a method to a class
#ff is defined outside the class, but we can bind it to a class
#using types.MethodType

class A:
    def __init__(self,x):
        self.x = x
def ff(self):
    print(self.x)
a   = A(11)
ffb = types.MethodType(ff,a)
ffb()   # notice the self argument is passed automatically to ffb()
'''
