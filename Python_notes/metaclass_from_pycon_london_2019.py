# -*- coding: utf-8 -*-


# https://www.youtube.com/watch?v=qqW4QYTeD40
# 19:11

class MyMeta(type):
    def __getitem__(self,key):
        print(key)
        
        
class Foo(metaclass=MyMeta):
    pass

# Foo does not define a __getitem__ method
# Neither does Foo inherit from anyone (Foo has no parents)
# But the dunder methods for an object are looked up in its class definition
# and the class definition of Foo is MyMeta
# So the dunder method __getitem__ gets looked up in
Foo['nachiket']

# Let us illustrate this with an example

class A:
    def __len__(self):
        print('Calling __len__ in class A')
        return 11
    
a = A()

# so __len__ is looked up in class A
print(len(a))


# we add a method __len__ in the object x
# but still the dunder method gets looked up in the class
a.__len__ = lambda x: 12
print(len(a))

# we can however explicitly call the dunder method associated with object a
print(a.__len__(13))
