# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:47:41 2020

@author: Gokhale
"""

# generator
def gen(n):
    while n>0:
        yield n
        n -=1
        
# processor
# you can modify the input stream        
def processor(numbers):
    for n in numbers:
        yield from [ ii for ii in range(n,n-3,-1)]

# consumer
rawnumbers   = gen(10)
processed    = processor(rawnumbers)
for ii in processed:
    print(ii,end=' ')