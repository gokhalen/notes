# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:23:40 2021

@author: aa
"""

from functools import wraps,partial

# Python Cookbook, Beazley and Jones, Chapter on decorators

# simple decorator
def decorate(func):
    # to get docstring and other attribs copied from func to wrapper.
    @wraps(func)  
    def wrapper(*args,**kwargs):
        print('-'*60)
        func()
        print('-'*60)
        
    return wrapper

# decorator which takes arguments
def decorate_args(prefix='',degree='',title=''):
    def decorate(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('-'*80)
            print(f'{prefix} {degree} {title} ',end='',sep='')
            func()
            print('-'*80)
            
        return wrapper
    return decorate

# Utility decorator to attach function as an attribute to an obj 
# last argument, func is the decorated function/
# first argument is the object to which func is to be attached
def attach_wrapper(obj,func=None):
    # see below for an explanation of this
    if func is None:
        return partial(attach_wrapper,obj)
    
    setattr(obj,func.__name__,func)
    # notice this - the decorated func is not modified
    return func

# IMPORTANT EXPLANATION 
# as per p.g. 341 in beazley jones the calling sequence for 
# decorators with arguments is 
# 
# func= attach_wrapper(obj=someting) (func)
#       ----------------------------
# the underlined is the first call to attach_wrapper
# since func is not defined, it is None
# the code goes to the first return and returns
# partial of attach_wrapper which accepts only once argument
# which is func
# this partial of attach_wrapper is called again


# pretty much the same decorator as before but with additional
# function attributes and non-local definitions
def decorate_adjustable_args(prefix='',degree='',title=''):
    def decorate(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('-'*80)
            print(f'{prefix} {degree} {title} ',end='',sep='')
            func()
            print('-'*80)
            
    
        @attach_wrapper(wrapper)
        def set_prefix(new_prefix):
            nonlocal prefix
            prefix = new_prefix
            
        @attach_wrapper(wrapper)
        def set_degree(new_degree):
            nonlocal degree
            degree = new_degree
            
        @attach_wrapper(wrapper)
        def set_title(new_title):
            nonlocal title
            title = new_title
            
        return wrapper

    return decorate


# decorator multiple use - can be used with or without args
# 
def decorate_multiple(func=None,*,prefix='A',degree='B',title='C'):
    
    # as per IMPORTANT EXPLANATION above
    # if used as 
    # 1) @decorate_multiple then the calling sequence is 
    # func = decorate_multiple(func)
    # func is the first positional argument - the decorator skips the first
    # return statement
    # if used as 
    # 2) @decorate_multiple(prefix='Herr',degree='Doctor',title='Professor')
    # the calling sequence is 
    # func = decorate_multiple(prefix='Herr',degree='Doctor',title='Professor')(func)
    # this first call does through the first return statement and partial of decorate_multiple
    # is returned, which then accepts func as a positional argument
    
    if func is None:
        return partial(decorate_multiple,prefix=prefix,degree=degree,title=title)
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('-'*80)
        print(f'{prefix} {degree} {title} ',end='',sep='')
        func()
        print('-'*80)
            
    return wrapper


# ----------------------------------------------------------------------------
# CASE 1
# print_nach gets passed as the last argument to decorate
# in this case it doesn't matter first and last are the same since
# there is only one argument, it matters for 
# @decorate
# def print_nach():
#    print('Nachiket Gokhale')
#    
# print_nach()
# ==--------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# CASE 2: Decorator which takes arguments
#
#
#@decorate_args(prefix='Herr',degree='Doctor',title='Professor')
#def print_nach():
#    print('Nachiket Gokhale')
#    
#print_nach()
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# CASE 3: Decorator which takes arguments which can later be customized
# 

# An amazing feature of this recipe is that the accessor functions will propagate through
# multiple levels of decoration (if all of your decorators utilize @functools.wraps). For
# example, suppose you introduced an additional decorator, such as the @timethis dec‐
# orator from Recipe 9.2, and wrote code like this:


'''
@decorate_adjustable_args(prefix='Herr',degree='Doctor',title='Professor')
def print_nach():
    print('Nachiket Gokhale')
    
print_nach()

# modify parameters
print_nach.set_prefix('Comrade')
print_nach.set_degree('Candidate of Science')
print_nach.set_title('Akademician')
print_nach()
'''

#----------------------------------------------------------------------------

@decorate_multiple(prefix='Herr',degree='Doctor',title='Professor')
def print_nach():
    print('Nachiket Gokhale')
    
print_nach()

@decorate_multiple
def print_nach():
    print('Nachiket Gokhale')
    
print_nach()



