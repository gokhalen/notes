# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:08:56 2021

@author: aa
"""

# Inspired by: extracting a subset of a dictionary in 
# David Beazley's Python Cookbook

# start with a simple list comprehension

nums = [1,2,3,4,5,6,7,8,9,10]
filt = [n if n < 5 else n*n for n in nums]

# let's try something similar with dictionaries
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

# this throws syntax error
# pfilt = {key:value if value > 11.00 for key,value in prices.items()}

# this works - seems you need the else branch
# pfilt = {key:value if value > 11.00 else 100 for key,value in prices.items()}

# and no you can't use modify the key on the left of the for
# the if on the left of the for is only modifying the value
# 'dummy_key':3.14 does not make sense - neither a string or and int 
# or another object in the current scope
# pfilt = {key:value if value > 11.0  else 'dummy_key':3.14 for key,value in prices.items()}


# you can do general purpose modifications of key,value pairs as follows
#def getkey(key,value):
#   return str(key) + str(value)

#def getval(key,value):
#    return str(key) + str(value)

#pfilt = {getkey(key,value):getval(key,value) for key,value in prices.items()} 