# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:04:49 2020

@author: Gokhale
"""

# A simple class
# Problem is that marks can be set to any value.
# We need accessors to control the getting and mutators to control the setting
class Student1:
    def __init__(self,marks):
        self.marks = marks

class Student2:
    def __init__(self,marks):
        self.marks = marks
    # properties are class level objects, 
    # can be accessed at object.__class__.marks 
    # or at Student2.marks
    # the tags @property, before def marks and @marks.setter before def marks
    # are creating a class level property object, 
    # named marks which controls what happens
    # when the one tries to set or get the attribute marks
    @property
    def marks(self):
        print('calling getter for marks')
        return self._marks
    
    @marks.setter
    def marks(self,marks):
        print('calling setter for marks')
        if marks > 100:
            marks = 100
        self._marks = marks

def marksproperty():
    # im pretty sure the @property and @prop.setter define a property object
    # inside marksproperty.  When this property object is returned
    # the getter and setter get bound to the object which catches the 
    # returned object
    # I can't seem to inspect functions the way I can inspect classes
    # e.g. Student2.marks says "<property at 0xc70c9a7f90>"
    # doing marksproperty.prop yields
    # 'function' object has no attribute 'prop'
    
    # since the propery object lives inside a class
    # the interpreter will pass an instance of the class
    # to the setter and getter when they are called
    @property
    def prop(self):
        print('calling getter for marksproperty')
        return getattr(self,'_marks')
    
    @prop.setter
    def prop(self,marks):
        print('calling setter for marksproperty')
        if marks > 100:
            marks = 100
        setattr(self,'_marks',marks)
        
    return prop
 
class Student3:
    # marks seems to be a class property object
    # can be located at object.__class__.marks 
    # or at Student3.marks
    # marks is a property returned by marksproperty
    # which, as before, controls what happens when the user tries 
    # to set or get marks
    marks = marksproperty()
    def __init__(self,marks):
        self.marks = marks
   

ss1 = Student1(150)
print(ss1.marks)
print('-'*20)
ss2 = Student2(150)
print(ss2.marks)
print('-'*20)
ss3 = Student3(150)
print(ss3.marks)
print('-'*20)

