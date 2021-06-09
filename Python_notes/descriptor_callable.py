# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:49:56 2021

@author: aa
"""

import types
 
class CallableDesc():
    def __init__(self):
        pass
        
    def __call__(self,*args):
        # self isthe instance of the Descriptor
        # args[0] is the instance of the student object
        # through args[0] the Descriptor has access to instance vars 
        # of class
        print(f'__call__ in CallableDesc {self=},{args=}')
        print(f'name={args[0].name}')
        print(f'marks={args[0].marks}')
        print(f'{args[1:]=}')
        
    def __set__(self,instance,value):
        instance.__dict__[self._name] = value
        
    def __get__(self,instance,cls):
        print('__get__ in CallableDesc')
        # since self is callable it is can be bound to instance
        return types.MethodType(self,instance)
    
class Student:
    desc = CallableDesc()
    def __init__(self,name,marks):
        self.name  = name
        self.marks = marks
        
s = Student('Nachiket','99')
s.desc(1,2,3,4)        
        
    
        
        
        