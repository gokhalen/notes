# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:55:34 2021

@author: User
"""

# https://stackoverflow.com/questions/62708756/mysterious-behaviour-of-python-built-in-method-filter-in-for-loop/62709033#62709033

func = lambda x: x != i  # i does not even need to exist yet

i = 3

# when func is executed i is looked up by the lambda
print(func(3))

# if you want to force binding do 
# now internal variable i is evaluated at define time to 3
func2 = lambda x,i=i: x != i

# changing i =5  does not make a difference
# i inside func2 is still bound to 3
i = 5

print(func2(5))
 


