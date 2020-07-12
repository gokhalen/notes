# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:27:29 2020

@author: Gokhale
"""


class Stock(object):
    
    def __init__(self,name:str,shares:int,price:float):
        self.name   = str.upper(name)
        self.shares = int(shares)
        self.price  = float(price)
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, number):
        self.shares -= number
        return self.shares
    
    def __str__(self):
        return f'({self.name},{self.shares},{self.price})'
    
    def __repr__(self):  
        return f'Stock({self.name},{self.shares},{self.price})'

goog = Stock('GOOG',100,490.2)
aapl = Stock('AAPL',200,1024.2)
# prints using the __str__  function
print(goog)
print(aapl)
# however, if we put it into a list or a tuple or any builtin container,
# the __repr__ function will be called on the contents of the container
ll = [goog, aapl]
print(ll)
