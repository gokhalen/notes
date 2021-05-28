# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:22:55 2021

@author: aa
"""

# https://www.geeksforgeeks.org/__new__-in-python/
# Seems that the trypical use of __new__ is to pass the Class (not its instance)
# to superclasses for fancy stuff

# in the following example, the __new__ method of super(AA,cls)
# probably calls __init__ of AA

# from gfg
# This means that if the super is omitted for __new__ method the
#  __init__ method will not be executed. Let’s see if that is the case.



class AA(object):
    def __new__(cls,x,y):
        print('new called, creating instance')
        return super(AA,cls).__new__(cls)
    def __init__(self,x,y):
        print('init called')
        self.x = x 
        self.y = y
        
a = AA(1.0,2.0)

# the following bombs out because,return cls(x,y) calls the 
# __new__ method of AA again, which calls the __new__ method of AA again
# and so on into an infinite recursion, which ends with max recursion depth
# being exceeded

class AA(object):
    def __new__(cls,x,y):
        return cls(x,y)