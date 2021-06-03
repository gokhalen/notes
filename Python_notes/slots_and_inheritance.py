# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:26:53 2021

@author: aa
"""
import sys

# Old link, but still useful info, it seems
# https://stackoverflow.com/questions/1816483/how-does-inheritance-of-slots-in-subclasses-actually-work
# Moral of the story is to be careful mixing __slots__ and inheritance
# Both Parent and child need to define __slots__ in order for it to work

'''
First item:

When inheriting from a class without __slots__, the __dict__ attribute of that
class will always be accessible, so a __slots__ definition in the subclass is 
meaningless.

Sixth item:

The action of a __slots__ declaration is limited to the class where it is
defined. As a result, subclasses will have a __dict__ unless they also define
 __slots__ (which must only contain names of any additional slots).
'''

# __slots__ seems to work by removing the __dict__ which each class has

# the following tries to set the x attribute and this is not allowed
# because 'x' is not in slots

#class Child:
#    __slots__ = ()
#    def __init__(self,x):
#        self.x = x
        
# fails        
# c = Child(1)

# print('-'*20,'exiting 1','-'*20)
# sys.exit()

# class Child:
#    __slots__ = ('x',)
#    def __init__(self,x):
#        self.x = x

# this works - x is in __slots__        
# c = Child(1) 
# this fails - y - is not in __slots__
# c.y = 12

####################################################################      

# First item
# Inheriting from a class without __slots__
# Dictionary of parent class is always accessible. So slots definition 
# in the subclass is meaningless


'''
class Parent:
    pass

class Child(Parent):
    # slots does not do anything meaningful as parent does not have slots
    __slots__ = ('x',)
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
c = Child(1.0,2.0)
c.z = 33
'''

########################################################################
# The action of a __slots__ declaration is limited to the class where it is
# defined. As a result, subclasses will have a __dict__ unless they also define
#  __slots__ (which must only contain names of any additional slots)

'''
class Parent:
    # this does not do anything because the childs dictionary is accessible 
    __slots__ = ('x',)
    
class Child(Parent):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
c = Child(2,3)
c.z = 33
'''
#############################################################################
# Both parent and child need to define __slots__ for it to work properly
'''
class Parent:
    __slots__ = ('x',)
    
    
class Child(Parent):
    # both following __slots__ defs work
    # __slots__ = ('x','y',)
    __slots__ = ('y',)
    def __init__(self,x,y):
        self.x = x
        self.y = y

# x and y are allowed to be set but z does not        
c   = Child(2,3)
c.z = 33
'''
############################################################################