# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:58:50 2020

@author: Gokhale
"""

from contextlib import contextmanager

class Counter:
    level=-1

@contextmanager
def idcongen(text):
    
    ctr = Counter()
    # if we do ctr.level +=1, it will create a new instance variable level
    # ctr.level += 1 is the same as ctr.level = ctr.level + 1
    # when the rhs is evaluated, there is no instance variable level, therefore 
    # it looks up the class variable. But on the lhs, it creates a new class var
    ctr.__class__.level += 1
    
    def printfunction(tt=text,ll=ctr.__class__.level):
        print(' '*8*ll + tt)
    
    
    # before yield, this is like the __enter__ method of a context manager class
    # we need something to set the level here depending on how many times
    # it is called
        
    yield printfunction
    
    # after yield, this is like the __exit__ method of the context man class
    ctr.__class__.level -=1
    
# this context manager prints indented
with idcongen('P1') as P1:
    P1()
    with idcongen('P2') as P2:
        P2()
    with idcongen('P3') as P3:
        P3()

with idcongen('P4') as P4:
    P4()
