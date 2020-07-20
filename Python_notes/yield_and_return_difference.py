# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:44:50 2020

@author: Gokhale
"""

def wrapper_return(n):
    return countdown(n)

def wrapper_yield(n):
    yield countdown(n)

def countdown(n):
    while n > 0:    
        yield n
        n -=1
        
if __name__ =='__main__':

    # wrapper_return __returns__ a generator function countdown
    # so gg is a generator function countdown    
    gg = wrapper_return(10)
    # presence of return statement and interpreter magic/language specification
    # ensures that gg is a generator object countdown
    print(gg)
    # we can iterate over that generator object, which yields numbers
    for ii in gg:
        print(ii)
    
    print(f'{"-"*25}')
    # wrapper_yield is itself a generator because of the yield statement. 
    # so gg is generator object wrapper_yield
    gg = wrapper_yield(10)
    print(gg)
    # what does wrapper_yield yield? It yields generator object countdown
    # so iterating over gg will only give the generator object countdown
    # the following loop will only give: generator object countdown
    for ii in gg:
        print(ii)
    
    print(f'{"-"*25}')
    # if we want values from countdown, we have to iterate over the 
    # generator object countdown itself like the following
    gg = wrapper_yield(10)
    for cd in gg:
        # cd is the generator object countdown yielded by wrapper_yield
        for ii in cd:
            print(ii)
