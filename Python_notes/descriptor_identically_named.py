# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:53:48 2021

@author: aa
"""

'''

Beazley and Jones, 'Python Cookbook' pg 298

If a descriptor will do nothing more than extract an
identically named value from the underlying instance dictionary, defining __get__()
is unnecessary.


'''

class Descriptor:
    
    def __init__(self,name=None,**opts):
        print('__init__ in Descriptor called')
        self.name = name
        for key,value in opts.items():
            setattr(self,key,value)
            
    # now this is a bit of black magic - 
    # there is no __get__ method, yet it behaves correctly.
    # the key part appears to be
    # "If a descriptor will do nothing more than extract an
    # identically named value from the underlying instance dictionary, defining __get__()
    # is unnecessary."
            
    def __set__(self,instance,value):
        print('__set__ in Descriptor called')
        instance.__dict__[self.name] = value
        
        
class Student:
    
    # the name of the Descriptor is 'name' (on the lhs)
    # and the dictionary key under which it is stored in the instance
    # dictionary is also 'name'
    
    name  = Descriptor('name')
    
    # the name of the descriptor is 'name2' but the name of the dictionary key
    # under which it is stored under the instance is 'name'
    name2 = Descriptor('name')
    
    def __init__(self,name):
        self.name   = name
        self.name2  = name
   
    
s = Student('Nachiket')
# this call works - inspite of there being no get method __get__
# the descriptor looks up the name of the descriptor i.e. 'name' in the 
# instance dictionary
print(s.name)
# it looks up 'name2' in the instance dictionary and since it does not find 
# it is simply returns self
print(s.name2)        


# finally in Student we have descriptors, but they are 
# storing values in the object dictionary under the same key ('name')
# the second value overwites the first
class Descriptor2:
    def __init__(self,name):
        self.name = name
                
    def __get__(self,obj,objname):
        if obj is None:
            return self
        else:
            return obj.__dict__[self.name]
        
    def __set__(self,obj,value):
        obj.__dict__[self.name] = value

class Student2:
    name = Descriptor2('name')
    age  = Descriptor2('name')
    
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        
s2 = Student2('Nachiket','41')
print(s2.name)
print(s2.age)        