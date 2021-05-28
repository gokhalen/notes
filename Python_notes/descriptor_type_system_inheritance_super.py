# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:02:34 2021

@author: aa
"""

import sys

# Base class. Uses a descriptor to set a value
class Descriptor:
    
    def __init__(self,name=None,**opts):
        print('__init__ in Descriptor called')
  
        self.name = name
        for key,value in opts.items():
            setattr(self,key,value)
            
    def __set__(self,instance,value):
        print('__set__ in Descriptor called')
        instance.__dict__[self.name] = value
        
# Descriptor for enforcing Types        
class Typed(Descriptor):
    expected_type = type(None)
    
    def __set__(self,instance,value):
        print('__set__ in Typed called')
        if not isinstance(value,self.expected_type):
            raise TypeError('expected'+str(self.expected_type))
        super().__set__(instance,value)
        
# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self,instance,value):
        print('__set__ in Unsigned called')
        if value < 0:
            raise ValueError('Expected >=0')
        super().__set__(instance,value)
        
class MaxSized(Descriptor):
    def __init__(self,name=None,**opts):
        print('__init__ in MaxSized called')
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name,**opts)
        
    def __set__(self,instance,value):
        print('__set__ in MaxSized called')
        if (len(value) >= self.size):
            raise ValueError('size must be <'+str(self.size))
        super().__set__(instance,value)

class Integer(Typed):
    expected_type = int
    
class UnsignedInteger(Integer,Unsigned):
    pass

class Float(Typed):
    expected_type = float
    
class UnsignedFloat(Float,Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String,MaxSized):
    pass
    
class Stock:
    name   = SizedString('name',size=8)
    shares = UnsignedInteger('shares')
    price  = UnsignedFloat('price')
    
    def __init__(self,name,shares,price):
        self.name   = name
        self.shares = shares
        self.price  = price
print('-'*80)
s = Stock('ACMEACM',50,float(91))    
print('-'*80)
print('-'*20,'Decorator','-'*20)
# sys.exit('First Exit')

def check_attributes(**kwargs):
    def decorate(cls):
        for key,value in kwargs.items():
            print(f'{key=},{value=}')
            if isinstance(value,Descriptor):
                # Here, 'value' is an instance of descriptor
                # simple key and value in the cls
                # print('In descriptor instance branch')
                value.name = key
                setattr(cls,key,value)
            else:
                # Here, 'value' is a Descriptor (not an instance)
                # just the Class. This occurs in the shares and price fields
                # So, you need to create the object of descriptor
                # Hence, value is called with the argument key 
                # to create the descriptor
                # print('In descriptor class branch')
                setattr(cls,key,value(key))
        return cls
    return decorate

@check_attributes(name=SizedString(size=8),shares=UnsignedInteger,price=UnsignedFloat)
class Stock2:
    def __init__(self,name,shares,price):
        self.name   = name
        self.shares = shares
        self.price  = price 

s=Stock2(name='ACME',shares=50,price=501.1)
         