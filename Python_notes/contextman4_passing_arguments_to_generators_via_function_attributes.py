# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:58:50 2020

@author: Gokhale
"""

from contextlib import contextmanager

class Counter:
    level=-1

def gen():
# gen.flag = True makes counter go forward
# gen.flag = False makes counter go backward    
    n=0
    while True:
        yield n 
        if gen.flag:
            n += 1
        if not gen.flag:
            n -= 1

gen.flag = True

gg = gen()

@contextmanager
def idcongen(text):
    
    # the generator needs to be pushed forward while entering the context
    
    gen.flag = True
    level    = next(gg)
    
    def printfunction(tt=text,ll=level):
        print(' '*8*ll + tt)
    
    
    # before yield, this is like the __enter__ method of a context manager class
    # we need something to set the level here depending on how many times
    # it is called
        
    yield printfunction
    
    # after yield, this is like the __exit__ method of the context man class
    # the generator needs to be pushed back while leaving the context
    gen.flag = False
    next(gg)
    
# this context manager prints indented
with idcongen('P1') as P1:
    P1()
    with idcongen('P2') as P2:
        P2()
    with idcongen('P3') as P3:
        P3()

with idcongen('P4') as P4:
    P4()
