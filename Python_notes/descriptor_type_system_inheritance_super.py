# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:02:34 2021

@author: aa
"""

import sys

# Beazley and Jones, 'Python Cookbook' 8.13 - pg 295+

# Base class. Uses a descriptor to set a value
class Descriptor:
    
    def __init__(self,name=None,**opts):
        print('__init__ in Descriptor called')
        self.name = name
        for key,value in opts.items():
            setattr(self,key,value)
            
    # now this is a bit of black magic - 
    # there is no __get__ method, yet it behaves correctly.
            
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

print('-'*80)
print('-'*20,'Metaclass Checker','-'*20)
print('-'*80)

# metaclass that applies checking
class checkedmeta(type):
    # this __new__ gets called coorectly because of metaclass magic
    def __new__(cls,clsname,bases,methods):
        # Attach attribute names to the descriptors
        print('Metaclass called during class definition')
        # methods.items() contains '
        # key='name'value=<__main__.SizedString object at 0x000001FBDA744970>
        # key='shares'value=<__main__.UnsignedInteger object at 0x000001FBDA744B20>
        # key='price'value=<__main__.UnsignedFloat object at 0x000001FBDA744FD0>
        # key='__init__'value=<function Stock3.__init__ at 0x000001FBDA86D940>
        for key,value in methods.items():
            print(f'{key=}{value=}')
            # if the object is a descriptor as defined earlier
            # set it's name attribute
            if isinstance(value,Descriptor):
                value.name = key
        return type.__new__(cls,clsname,bases,methods)
    
class Stock3(metaclass=checkedmeta):
    # note - unlike Stock, we are not assigning the name with which 
    # the descriptor stores the variables in the object
    # the definition in Stock is name   = SizedString('name',size=8)
    # name is missing on the rhs
    
    # when the metaclass code is executed, the descriptor objects on
    # the rhs are going to have their name attribute set to name,shares
    # or price
    
    name   = SizedString(size=8)
    shares = UnsignedInteger()
    price  = UnsignedFloat()
    
    def __init__(self,name,shares,price):
        self.name   = name
        self.shares = shares
        self.price  = price
    
         