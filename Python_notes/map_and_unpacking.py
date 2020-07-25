# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:15:49 2020

@author: aa
"""

import itertools 
import collections.abc

def ff(x,y,z):
    return x+y+z

#define iterables
l1=list(range(5))
l2=list(range(5))
l3=list(range(5))

# map can accept multiple arguments
# this just creates a map object which is an iterable
a=map(ff,l1,l2,l3)

for item in a:
    print(item,end=' ')

print('')    
# however, we can unpack it by defining the lhs correctly

(a1,a2,a3,a4,a5) = map(ff,l1,l2,l3)
print(f'{a1=},{a2=},{a3=},{a4=},{a5=}')

[a1,a2,a3,a4,a5] = map(ff,l1,l2,l3)
print(f'{a1=},{a2=},{a3=},{a4=},{a5=}')

# if you want to unpack it into an array
# first value goes into a1, last into a3 remaining into a2
(a1,*a2,a3) = map(ff,l1,l2,l3)
print(f'{a1=},{a2=},{a3=}')

# two or more starred expressions not allowed
#(a1,*a2,*a3) = map(ff,l1,l2,l3)

# there is only one variable which is starred. Whatever that "remains" goes 
# into a1. Since there is no other variable, whatever that "remains" is
# everything. Therefore, everything goes into a1
*a1, = map(ff,l1,l2,l3)

# unpacking on the rhs
ll = [*l1, *l2, *l3, *map(ff,l1,l2,l3)]
print(f'{ll=}')

# how does unpacking work when length of iterables is not known?
# it seems to wait for the shortest iterable to get exhausted, compute 
# the sequence and then assign it to the lhs
it=range(5)
(a1,*a2,a3)=map(ff,it,it,it)
print(f'{a1=},{a2=},{a3=}')

# but we have a problem. I would have expected the last output to be 
# 0 + 1 + 2 = 3. That is, I would have expected map to call 'next' on the 
# first 'it' get 0, then call 'next' on the second 'it' and get '1' since 
# the second 'it' points to the same range object, and then get '2' from
# the third 'it'. I would have expected the iterators to be exhausted
# the second time around. But, I think the point to note is that range
# is an iterable, not an iterator. I think map makes iterators out of the 
# range object by calling iter on it. Two separate iterators are created,
# which is why they are not linked. You can test this.

rr=range(5)
it1=iter(rr)
it2=iter(rr)
print(next(it1))
print(next(it2))

# both yield zero

# now let us construct an actual, real iterator
class MyIter():
    
    def __init__(self,start=0,end=5):
        self.start=0
        self.end=end
        self.num=start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if ( self.num == self.end ): 
            raise StopIteration('Iterator exhausted')
        
        num = self.num
        self.num += 1
        return num


obj = MyIter()
# since the __iter__ method returns self all three iterators point to the same obj
it1 = iter(obj)
it2 = iter(obj) 
it3 = iter(obj)

# try calling next(it1),next(it2),next(it3) to see they return 0,1,2

# the below crashes and burns. for the first pass, it1, it2 and it3 return
# 0,1,2. (0+1+2) = 3 is produced. In the second pass the iterator is exhausted
# So only one value is produced, but we need 2 values: 1 in a1, 1 in a3 and 
# remaining in a2 (which can be empty). So this works as we originally expected
# note: if we modify the __iter__ method in MyIter to return 'iter(range(5))' 
# things will work as before...

#(a1,*a2,a3)=map(ff,it1,it2,it3)
#print(f'{a1=},{a2=},{a3=}')
