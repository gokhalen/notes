# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:17:39 2021

@author: aa
"""

import sys

# Based on Python Cookbook, Beazley Jones 2013, pg. 224

# the idea is that we define variable names in PolyHeader
# Their values are assigned from a list, which mimics 
# the _buffer used in the Cookbook. By defining 
# only the variable name and size in a class which 
# inherits from Structure, we automatically get all the 
# machinery to create named variables

# With this inheritance pattern, StructureMeta is called twice,
# before any objects are created, once for Structure and once for
# PolyHeader

# the output is
#__init__ in StructureMeta called
#self=<class '__main__.Structure'>,clsname='Structure',bases=(),clsdict={'__module__': '__main__', '__qualname__': 'Structure', '__init__': <function Structure.__init__ at 0x0000026C2B46AD30>}
#__init__ in StructureMeta called
#self=<class '__main__.PolyHeader'>,clsname='PolyHeader',bases=(<class '__main__.Structure'>,),clsdict={'__module__': '__main__', '__qualname__': 'PolyHeader', '_fields_': [('name', 8), ('age', 2)]}

# this shows, 'self' is a class, not an object instance.



class StructureMeta(type):
    def __init__(self,clsname,bases,clsdict):
        print(' __init__ in StructureMeta called')
        print(f'{self=},{clsname=},{bases=},{clsdict=}')
        
    
class Structure(metaclass=StructureMeta):
    def __init__(self,ss):
        print('__init__ in Structure called')
        self._string = ss
        
       
class Student(Structure):
    # the field 'name' is 8 chars
    # the field 'age'  is 2 chars
    _fields_ = [('name',8),('age',2)]
    
    
sys.exit()


# let's create objects and see what is called

# uncomment this
# phead = PolyHeader(['Nachiket41'])

# sys.exit()

# only the __init__ in Structure is called. 
# __init__ in the metaclass is not called


# Let's modify the previous a little bit more
# Specifically, let us introduct the variable 'struct_size'
# which will be the sum of lengths of 'name' and 'age' i.e.
# 8+2 = 10

class StructField:
    '''
    Descriptor representing a simple structure
    '''
    def __init__(self,datasize,offset):
        # offset is the offset from which to read data
        self.offset   = offset
        self.datasize = datasize
        
    def __get__(self,obj,cls):
        # here self refers to an instance of the descriptor
        # obj is the instance of the object which holds the descriptor
        # cls is the class of the object which holds the descriptor
        if obj is None:
            # I don't understand this
            # it just seems to return the instance of the descriptor if
            # obj is None. Probably not important for now.
            return self
        
        else:
            return obj._string[self.offset:self.offset+self.datasize]
        

class StructureMeta(type):
    def __init__(self,clsname,bases,clsdict):
        print('__init__ in StructureMeta called')
        print(f'{self=},{clsname=},{bases=},{clsdict=}')
        # self is a class, not an object instance
        # so the following line gets the attribut _fields_
        # from the class instance
        fields = getattr(self, '_fields_', [])
        
        offset = 0
        for name,size in fields:
            # create data descriptor - remember self is a class
            setattr(self,name,StructField(size,offset))
            offset = offset+size
            
        # since self is a class, and not an instance for which (self)
        # is used, struct_sizeis created when PolyHeader class 
        # is defined
        self.struct_size = offset
    
class Structure(metaclass=StructureMeta):
    def __init__(self,ss):
        print('__init__ in Structure called')
        self._string = ss
        
class Student(Structure):
    # the field 'name' is 8 chars
    # the field 'age'  is 2 chars
    _fields_ = [('name',8),('age',2)]
    
student = Student('Nachiket41 xfsdtfge')
print(student.name)
print(student.age)
