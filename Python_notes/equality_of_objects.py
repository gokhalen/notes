# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:33:10 2021

@author: aa
"""

# two objects of the same class are not equal unless 
# the __eq__ method has been defined

# exception: if the objects are the same object then true is 
# returned

class Singleton(type):
    def __init__(self,*args,**kwargs):
        self.__instance = None
        super().__init__(*args,**kwargs)
        
    def __call__(self,*args,**kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args,**kwargs)
            return self.__instance
        else:
            return self.__instance
            
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')
        
        
s1 = Spam()
s2 = Spam()
# s1 and s2 are the same object - Singletons
print(f'{(s1==s2)=}')
print(f'{(s1 is s2)=}')

class A:
    pass


a = A()
b = A()

print(f'{(a==b)=}')  # False, not the same object
print(f'{(a==a)=}')  # True, same object
print(f'{(a is b)=}')
print(f'{(a is a)=}')