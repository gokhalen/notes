# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:41:34 2021

@author: aa
"""

# Beazey Jones "Python Cookbook" pg 283
class Integer:
    def __init__(self,name):
        # self.name is the key searched for in the dictiona
        self.name = name
        
    def __get__(self,instance,cls):
        if instance is None:
            # If you call this from Class Student instead of an instance of Student
            # the instance of the descriptor will be returned
            # this might enable one to make modifications to the 
            # instance of descriptor
            return self
        else:
            return instance.__dict__[self.name]
        
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
                
class Student:
    marks = Integer('99')
    
class Point:
    x = Integer('a')
    y = Integer('b')
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point({self.x},{self.y})'
    
p = Point(2,3)

# now if you do strange things like 
# p.__class__.x = 1, you are effectively overriding the descriptor, replacing
# it with a number
# don't do these strange things
    
        
    
        