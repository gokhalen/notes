# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:27:25 2021

@author: aa
"""

# Beazey Jones "Python Cookbook" pg 284

# descriptor for a type checked attribute
class Typed:
    def __init__(self,name,expected_type):
        self.name = name
        self.expected_type = expected_type
        
    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
        
    def __set__(self,instance,value):
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected' + str(self.expected_type))
            
        instance.__dict__[self.name] = value
        
    def __delete__(self,instance):
        del instance.__dict__[self.name]
        
# class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate

# example use
@typeassert(name=str,shares=int,price=float)
class Stock:
    def __init__(self,name,shares,price):
        self.name   = name
        self.shares = shares
        self.price  = price
        
    
