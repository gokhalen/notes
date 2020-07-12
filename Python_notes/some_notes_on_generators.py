# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:18:26 2020

@author: Gokhale
"""

def gen1():
    n = 0
    while True:
        yield n
        n +=1

# always prints zero, because a new generator object  is created everytime        
print(next(gen1()))
print(next(gen1()))
print(next(gen1()))
print(next(gen1()))


print('-'*25)
data1 = iter(range(16))
def gen2(data):
    for d in data:
        yield d

# this prints 0,1,2,3. At first glance, this behavior seems contradictory
# to gen1. But not really. Even though a new gen2 generator is created
# everytime, the for call inside gen2 has consumed data from data1 
# because data1 is an iterator
print(next(gen2(data1)))
print(next(gen2(data1)))
print(next(gen2(data1)))
print(next(gen2(data1)))

# we can see this by directly printing the next value from data1 
print(next(data1)) 
