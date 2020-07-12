# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:26:03 2020

@author: Gokhale
"""

dd={'name': 'GOOG', 'shares': 100, 'price': 490.1}
dd2={'address':'Chicago, IL'}
dd3={'sport':'cricket'}
def ff(**kwargs):
    print(kwargs)
    
    
def ff2(name='AAPL',shares=250,price=901.34,address='New York, NY'):
    print(name,shares,price,address)

# this causes error: ff() takes 0 positional arguments but 1 was given
# ff(dd)

ff(**dd)
ff(**dd,**dd2)
ff(name='Nachiket',address='Pune,India')

ff2(**dd)
ff2(**dd,**dd2)
ff2(**dd,address='Boston,MA')
# Not allowed. Unexpected argument 'sport'
# ff2(**dd3)
# positional argument follows keyword argument unpacking
# ff2(**dd,1)

# moral: 
# 1) if you use **kwargs to catch arguments, they must be unpacked
#    they will be stored into the dictionary kwargs
# 2) if you use named keywords to catch arguments, and pass dictionaries,
#    they must still be unpacked. unexpected arguments are not allowed
# 3) You cannot simply pass dictionaries and expect keys to be converted 
#    to variable names and values to the values of those names 
