# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:45:45 2021

@author: aa
"""

class DescriptorName(object):
    
    def __init__(self,name='John',descname='name'):
        print('__init__ called in DescriptorName')
        self.name     = name
        self.descname = descname 
        
    def __get__(self,obj,objtype):
        print('__get__ called in DescriptorName')
        setattr(obj,self.descname,self.name)
        return self.name
    
    #def __set__(self,obj,name):
    #    print('__set__ called in DescriptorName')
    #    self.name = name
 
        
class GFG(object):
    name = DescriptorName()
    
g1 = GFG()
# __get__ of DescriptorName is called for this call
print(g1.name)
# __get__ of DescriptorName is NOT called for this call
print(g1.name)

# if __set__ method is uncommented then __get__ will be called for both calls
