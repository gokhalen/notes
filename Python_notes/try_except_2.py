# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:04:38 2020

@author: Gokhale

Exception classes are instantiated when raised

"""


class FormatError(Exception):
    
    def __init__ (self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None
        print('__init__ in FormatError called')
    
    def __str__(self):
        print('calling str')
        if self.message:
            return f'FormatError,{self.message}'
        else:
            return 'FormatError has been raised'
    
    pass

# this will print: __init__ in FormatError called
try:
    raise FormatError("xls file not supported")
except:
    pass

# this will aslo print: __init__ in FormatError called
# e is an instance of FormatError 
# with the arguments with which raise calls FormatError
try:
    raise FormatError("xls file not supported")
except FormatError as e:
    pass

