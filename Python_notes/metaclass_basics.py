# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:16:54 2021

@author: aa
"""

# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
# See diagram under 'Putting it all together'


# without inheriting from type super() calls don't work
# type is not automatically the parent, it needs to be specified
class Meta(type):
    
    # just like normal classes have a __new__ method, 
    # metaclasses do so too
    # this delegates to type, which does the right thing
    # I think if __new__ is not defined it is inherited from type
    def __new__(cls,clsname,bases,clsdict):
        print('Calling __new__ in Meta')
        print(f'{cls=},{clsname=},{bases=},{clsdict=}')
        print('-'*80)
        return super().__new__(cls,clsname,bases,clsdict)
            
    def __init__(self,clsname,bases,clsdict):
        # this gets called when Normal class is defined with four arguments
        # Since a class is an instance of MetaClass,
        # defining a class amounts to creating an instance of MetaClass
        print('Calling __init__ in Meta')
        # self is an instance of Meta (which is the class Normal)
        # We can programmatically add attributes to self (class Normal)
        # p.g. 279 in Beazley Jones Python Cookbook
        print(f'{self=},{clsname=},{bases=},{clsdict=}')
        print('-'*80)
        
        # Can also do the following if you'd like   
        # super().__init__(clsname,bases,clsdict)

    
    def __call__(self,*args,**kwargs):
        # arguments from __init__ in Normal are forwarded here
        print('Calling __call__ in Meta')
        print(f'{self=},{args=},{kwargs=}')
        print('-'*80)
        

        # I think you can manually manage __new__ and __init__ of Normal from
        # here, or you can get type (parent of Meta) to do it using the following call
        # If you do it manually, you need to be careful about passing 
        # self and cls corectly
        
        super().__call__(*args, **kwargs)
        pass
    
    @classmethod
    def __prepare__(cls,clsname,bases):
        # This method is called before the class body is executed
        # and it must return a dictionary-like object that's used as
        # the local namespace for all the code from the class body.
        
        # the returned dictionary becomes clsdict in the __new__ method of this class
        # (Meta)
        
        print('Calling __prepare__ in Meta')
        print(f'{cls=},{clsname=},{bases=}')
        print('-'*80)
        return {}
    
    
    
class Normal(metaclass=Meta):
    def __new__(cls,x):
        print('Calling __new__ in Normal')
        print(f'{cls=},{x=}')
        print('-'*80)

        # super of Normal is NOT Meta, it is object
        # you can check Normal.__mro__
        # you can call __init__ as below
        return super(Normal,cls).__new__(cls)
        # doing the following is going to be an infinite recursion
        # because cls(x) will call __new__, which will call cls and so on
        # return cls(x)
    
    def __init__(self,x):
        # arguments
        print('Calling __init__ in Normal')
        print(f'{self=},{x=}')
        print('-'*80)


# https://stackoverflow.com/questions/45536595/understanding-call-with-metaclasses
# See MSeifert's answer
# To create an object, we 'call' the Class of the object
# But the Class of the Object itself is an instance of metaclass
# So, the __call__ method from the metaclass gets looked up first while creating
# the object n
print('-'*10,'compile time initializations done','-'*10)
print('-'*80)
n = Normal('nachiket')