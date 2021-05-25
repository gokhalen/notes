# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:55:07 2021

@author: aa
"""

# p.g. 253 Python Cookbook

from queue import Queue
from functools import wraps

'''
def coro():
    a = yield 1
    print(f'in coro {a=}')
    b = yield 2
    print(f'in coro {b=}')
    c = yield 3
    print(f'in coro {c=}')
    
c = coro()
print(c.send(None))
print(c.send('aa'))
print(c.send('bb'))
print(c.send('cc'))
'''

def apply_async(func,args,*,callback):
    result = func(*args)
    callback(result)
    
class Async:
    def __init__(self,func,args):
        self.func = func
        self.args = args
        
def inlined_async(func):
    # wraps makes wrapper look like func.
    # i.e. __docs_, __name__ possibly __annotations__
    # are copied from func to wrapper
    @wraps(func)
    def wrapper(*args):
        f = func(*args)         # creates a generator from generator definition
        result_queue = Queue()  # creates a threaded multi-producer, multi-consumer queue
        result_queue.put(None)  # first value in the queue is None
        
        while True:
            result = result_queue.get()  # get the first value in the queue
            try:
                # for the first time through the while loop
                # result is None, which is exactly what we want to start the generator
                # the generator is going to yield what we tell it to yield
                # after the first call to send, values are going to be assigned
                # to the lhs of the yields see commented example 
                # once assigned they are going to be printed
                a = f.send(result)          
                apply_async(a.func,a.args,callback=result_queue.put)
                
            except StopIteration:
                # when there are no more yields left, the generator returns None
                # stop iteration is raised (f.send(result)) is the thing 
                # which actually causes the StopIteration
                # since we are catching the exception, it gracefully exits
                break
                
    return wrapper
                    
def add(x, y):  
    return x + y

@inlined_async
def test():
    print('Starting')
    r = yield Async(add,(2,3))
    print(r)
    r = yield Async(add,('hello','world'))
    print(r)
    for n in range(10):
        r = yield Async(add,(n,n))
        print(r)
    print('Goodbye')
    
