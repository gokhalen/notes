# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:27:58 2021

@author: aa
"""

class DescriptorName(object):
    
    def __init__(self,varname):
        print('__init__ called in DescriptorName')
        self.varname = varname
        
    def __get__(self,obj,objtype):
        print('__get__ called in DescriptorName')
        print(obj,objtype)
        return getattr(obj,self.varname)
    
    def __set__(self,obj,value):
        print('__set__ called in DescriptorName')
        setattr(obj,self.varname,value)
        
        
class DescriptorAge(object):
    def __init__(self,age='3.14'):
        print('__init__ called in DescriptorAge')
        self.age = age
        
    def __get__(self,obj,objtype):
        print('__get__ called in DescriptorAge')
        return f'{self.age} for {self.age}'
    
    def __set__(self,obj,age):
        print('__set__ called in DescriptorAge')
        self.age = age

        
        
class GFG(object):
    # every instance of GFG points to the same instances of descriptors
    # because Descriptors are typically 'class variables'
    # so if you store variables in an instance of a descriptor
    # then they are going to be shared across instances of GFG 
    # here the descriptor name stores variables inside instances (obj)
    
    # descriptor DescriptorName stores variables in the object - therefore this 
    # information is not shared across instances
    # descriptor DescriptorAge stores variables in itself. This information
    # is shared across instances.
    
    
    name = DescriptorName('_name')
    age  = DescriptorAge()
    
    def __init__(self,name):
        self.name = name
    
g1 = GFG('John')
g2 = GFG('Paul')

# different names are seen
print('-'*80)
print(f'{g1.name=}')
print(f'{g2.name=}')
print('-'*80)

g1.age = 31
g2.age = 41

# both ages are 41
print('-'*80)
print(f'{g1.age=}')
print(f'{g2.age=}')
print('-'*80)

# This is illustrated in the example below
# Class BB contains **'instances'** of class AA
# So, all instances of BB point to the same instance of class AA

# So when we modify p1 in b1, the change is reflected in b2 as well

class AA():
    def __init__(self):
        self.x = 1
        self.y = 2
        
    def __str__(self):
        return f'({self.x},{self.y})'

class BB():
    p1 = AA()
    

b1 = BB()
b2 = BB()
print(b1.p1)
print(b2.p1)
b1.p1.x = 11
b1.p1.y = 22
print(b1.p1)
print(b2.p1)
