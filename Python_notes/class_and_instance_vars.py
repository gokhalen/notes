# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:00:38 2020
@author: Gokhale

instance and class variables

"""

class MyClass():
    # class variable
    xx = 111
    
    def __init__(self,var):
        self.xx = var


class MyClass2():
    __slots__ = ('xx',)
    
    def __init__(self,var):
        self.xx = var

'''        
# this definition is not allowed
ValueError: 'xx' in __slots__ conflicts with class variable

class MyClass3():
    __slots__ = ('xx',)
    xx = 111
    def __init__(self,var):
        self.xx = var
'''
aa = MyClass(222)
bb = MyClass2(444)



# this prints 222, indicating instance vars get priority in lookup
print(aa.xx)

# this prints 111
print(aa.__class__.xx) 

# this deletes instance variable
del aa.xx

# this prints the class variable
print(aa.xx)

# this deletes the class variable
# note del aa.xx will raise attribute error
del aa.__class__.xx

print(f'{"_"*10}')
# AttributeError for both
# print(aa.xx)
# print(aa.__class__.xx)

# This yields 444
print(bb.xx)
bb.__class__.xx = 555

# This yields 555 which is opposite to the behavior in previous case
# Moral of the story: Do not mess around with __slots__ and 
# class variables of the same name 
print(bb.xx)


