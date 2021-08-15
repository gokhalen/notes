# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:49:37 2021

@author: aa
"""

import sys

class Base(object):
    def __new__(cls,basename,basemarks):
        print('__new__ in Base')
        cls.basemarks = basemarks
        return super(Base,cls).__new__(cls)
    
    def __init__(self,basename,basemarks):
        print('__init__ in Base')
        self.basename = basename
        
class Child(Base):
    def __new__(cls,name,basename,marks,basemarks):
        print('__new__ in Child')
        cls.marks = marks
        # notice - cls is passed to __new__  unlike __init__ below
        return super(Child,cls).__new__(cls,basename,basemarks)
    
    def __init__(self,name,basename,marks,basemarks):
        print('__init__ in Chiild')
        self.name = name
        
        # notice  - self is not passed to init unlike __new__ above
        super(Child,self).__init__(basename,basemarks)
        # or super().__init_(basename,basemarks)


# in Child, __new__ and __init__ take the same arguments which are given 
# by the user when they're instantiated
# this could be changed, but then __new__ and init would need to be called manually
# see below

c = Child('nachiket','gokhale',89,100)
print(f'{c.name=},{c.basename=},{c.marks=},{c.basemarks=}')        
        
sys.exit()
        
# __init__ and __new__ do not take the same arguments        
class Student():
    def __new__(cls,name,surname):
        cls.name    = name
        cls.surname = surname
        return super(Student,cls).__new__(cls)
    
    def __init__(self,marks):
        self.marks = marks             

# throws an error because new is called with only one argument - marks        
# s = Student(89.0)

# instead, do
s = Student.__new__(Student,'Nachiket','Gokhale')
s.__init__(89.1) 

print(f'{s.name=},{s.surname=},{s.marks=}')

 