# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:17:39 2021

@author: aa
"""

import sys

# Based on Python Cookbook, Beazley Jones 2013, pg. 224
# This builds on metaclass_explanation.py to include nested 
# structures


class StructField:
    '''
    Descriptor representing a simple structure
    '''
    def __init__(self,datasize,offset):
        # offset is the offset from which to read data
        self.offset   = offset
        self.datasize = datasize
        
    def __get__(self,obj,cls):
        print('__get__ called in StructField')
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
        
class NestedStruct:
    '''
    Descriptor representing (phys,chem,math)
    '''
    def __init__(self,name,struct_type,offset):
        print('__get__ called in NestedStruct')
        # name is the name given in Polyheader
        # struct_type is Marks (can be other things)
        self.name        = name
        self.struct_type = struct_type
        self.offset      = offset
        
    def __get__(self,obj,cls):
        if obj is None:
            return self
        else:
            # we create an object from struct_type and put it in obj 
            # with name self.name
            result = self.struct_type(obj._string[self.offset:self.offset+self.struct_type.struct_size])
            # As long as the __set__ method does not exist in the descriptor
            # the __get__ method will not be called if the attribute has been set
            # using setattr. see descriptor_setattr.py
            # setattr(obj,self.name,result)
            return result

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
            
            # size is an int, StructField descriptor can be created
            if (isinstance(size,int)):
                # create a standard descriptor in the class
                setattr(self,name,StructField(size,offset))
                offset = offset+size
                
            # size it is a instance of Marks (which is an instance of StructureMeta)
            if (isinstance(size,StructureMeta)):
                # create a descriptor of the NestedStructure in the class
                setattr(self,name,NestedStruct(name,size,offset))
                offset = offset + size.struct_size
            
        # since self is a class, and not an instance for which (self)
        # is used, struct_sizeis created when PolyHeader class 
        # is defined
        self.struct_size = offset
    
class Structure(metaclass=StructureMeta):
    def __init__(self,ss):
        print('__init__ in Structure called')
        self._string = ss
        
class Marks(Structure):
    # the field 'phys' is 2 chars
    # the field 'chem' is 2 chars
    # the field 'math' is 2 chars
    _fields_ = [('phys',2),('chem',2),('math',2)]
        
       
class Student(Structure):
    # the field 'name' is 8 chars
    # the field 'age'  is 2 chars
    
    # change 'data' string below accordingly
    #_fields_ = [('name',8),('age',2),('marks',Marks)]
    _fields_  = [('name',8),('marks',Marks),('age',2)]    

name = 'Nachiket'
age  = '41'
phys = '89'
chem = '83'
math = '96'

#data = f'{name}{age}{phys}{chem}{math}'+'xfsdtfge'
data = f'{name}{phys}{chem}{math}{age}'+'xfsdtfge'


print('-'*80)
print('Creating student object')
student = Student(data)
print('-'*80)

# most of the __get__ calls are after the student object has been created

print(f'{student.name=}')
print(f'{student.age=}')
print(f'{student.marks.phys=}')
print(f'{student.marks.chem=}')
print(f'{student.marks.math=}')
