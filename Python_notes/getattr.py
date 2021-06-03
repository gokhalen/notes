# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:19:40 2021

@author: aa
"""

# Beazley and Jones, 'Python Cookbook' pg. 308

# __getattr__ does not apply to dunder methods

class A:
    def spam3(self,x,y,z):
        print('A.spam3 ',x,y,z)
        
    def spam(self,x):
        print('A.spam ',x)
        
        
class B:
    def __init__(self):
        self._a = A()
        
    def __getattr__(self,name):
        # First, the __getattr__() method is actually a fallback method that only gets called when
        # an attribute is not found.
        # the name argument is actually the name of the attribute to get
        # in the following examples name would be 'spam' or 'spam3'
        print('name=',name)
        return getattr(self._a,name)
    
b = B()
b.spam(11)
b.spam3(11,12,13)