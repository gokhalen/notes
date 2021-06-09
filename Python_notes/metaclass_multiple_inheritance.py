# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:01:58 2021

@author: aa
"""

from inspect import signature
import logging

# Beazley Jones, Python Cookbook, p.g. 369

# __init__ in MatchSignaturesMeta is called once for Root,A,B in that sequence
# self will be class Root, class A, and class B in that sequence
# self is an instance of MatchSignaturesMeta (instance can be Root,A or B)
# definition of super(self,self) changes accordingly

class MatchSignaturesMeta(type):
    def __init__(self,clsname,bases,clsdict):
        # who is super() - type?
        print(f'In Meta __init__: {self=},{clsname=},{bases=},{clsdict=}')
        # super does not seeem to print useful info.
        # MatchSignaturesMeta.__mro__ gives more useful into
        # The MRO is, as expected, (__main__.MatchSignaturesMeta, type, object)
        print(f'In Meta __init__: {super()=}')
        super().__init__(clsname,bases,clsdict)
        # self is the Class Root
        sup = super(self,self)
        print(f'In Meta __init__: {sup=}')

        
        for name,value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig  = signature(value)
                if prev_sig != val_sig:
                    print(f'Signature mismatch: {value.__qualname__},{prev_sig},{val_sig}')
                    
        print('-'*80)
                    
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass
    def spam(self, x, *, z):
        pass    

class B(A):
    def foo(self, a, b):
        pass
    def spam(self,x,z):
        pass

    