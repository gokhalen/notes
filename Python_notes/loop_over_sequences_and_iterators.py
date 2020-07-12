# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:48:55 2020

@author: Gokhale
"""
'''
Note: a list is not an iterator. it does not implement the __next__ method
One can get a iterator from a list by using __iter__ or calling iter()
the following code will start looping right from the start i.e. again from 1
'''
ll = list(range(10))        # can also do ll = tuple(range(10))
for ii in ll:   
    if ii == 5:
       break
    print("ii=",ii)
    
for ii in ll:
    print("ii=",ii)

'''
the following code will start looping from the middle
'''    
columns = ['name','shares','price','account']
values  = ['GOOG',100,490.1, 12345 ]
pairs   = zip(columns,values)

for ss,pp in pairs:
    print(ss,pp)
    if (ss == "name"):
        break
print('after first for loop')
for ss,pp in pairs:
    print(ss,pp)
    
'''
after an iterator finishes iterating, it can't be reset (easily)
the following code will produce no output
'''
for ss,pp in pairs:
    print(ss,pp)
    
print("no output from iterator without resetting")

pairs = zip(columns,values) #create new iterator
for ss,pp in pairs:
    print(ss,pp)

print("finished output from new iterator")

# you can create a new object to iterate over by
for ss,pp in zip(columns,values):
    print(ss,pp)

print("finished iterating over dynamically created object")

for ss,pp in zip(columns,values):
    print(ss,pp)
