# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:35:52 2021

@author: aa
"""

import operator
import types
import sys

# this function is going to return a class, which extends the 
# functionality of tuple
# hence tuple.__new__ is called by __new__ 
# if we were directly subclassing tuple we would do super().__new__
def named_tuple(classname,fieldnames):
    # for every name we are creating a property
    # if we make a class named_tuple('Point',['x','y'])
    # 'x' and 'y' are going to be mapped to properties 'x' and 'y'
    # property x will be itemgetter(0)
    # property y will be itemgetter(1)
    # when we do p.x it will return itemgetter(0)(self) = self[0]
    
    # basically storage is handled by the main tuple class
    # and the hack with itemgetter emunates named attributes
    
    cls_dict = {
                name: property(operator.itemgetter(n)) 
                for n,name in enumerate(fieldnames) 
                }
    
    def __new__(cls,*args):
        if len(args) != len(fieldnames):
            raise TypeError(f'Expected {len(fieldnames)} arguments')
            
        # the class returned by this func
        return tuple.__new__(cls,args)
    
    cls_dict['__new__'] = __new__
    
    cls = types.new_class(classname,(tuple,),{},lambda ns: ns.update(cls_dict)
                          )
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


Point = named_tuple('Point',['x','y'])