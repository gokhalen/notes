# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:33:13 2020

@author: Gokhale
"""
# David Perlman's comment
# https://stackoverflow.com/questions/509211/understanding-slice-notation
# and variations thereof

# List slicing creates a shallow copy of the list
# Be careful while dealing with lists of lists

# remove entries indexed 2,3 and insert [1,2,3] starting at pos 2
p      = ['a','b','c','d','e','f']
p[2:4] = [1,2,3]
#print(p)
#print('-'*40)

# replace the 2th index and insert the list there
p=['a','b','c']
p[2:4]=['e','f','g']
#print(p)
#print('-'*40)

# surprising: since the step is +1 we can't get from -1 to -3
# python appears to preserve c
p=['a','b','c']
p[-1:-3]=['e','f','g']
#print(p)
#print('-'*40)

# negative indices for list assignment
p=list(range(10))
# this produces error
# when extended slices are used the array assigned and array deleted
# have to be of the same size
# https://stackoverflow.com/questions/62595629/list-slice-assignment-with-resize-using-negative-indices
#p[-2:-5:-1]=[1,2]
# but this this resizes list 
#p[2:5:1]=[1]
# asked reason on SO
# print(p)
# print('-'*40)

# more surprising
# when we try to assign to list indices out of range,
# the results will be added to the end
p=['a','b','c']
p[11:12]=['d','e','f']
#print(p)
#print('-'*40)
# if your indices are out of bounds on the negative side
# results are added to the left
p[-11:-8]=['p','q','r']
#print(p)
# print('-'*40)

# what happens when indices overlap?
# result is as expected, consistent with deleting entries 
# starting with start
p=['a','b','c']
p[2:4]=['d','e','f']
#print(p)
# print('-'*40)

# what happens when overlap is on the negative side
# it seems to keep the entry indexed -2, deletes -3
# consistent with deleting entries befor "end"
p=['a','b','c']
p[-5:-2]=['d','e','f']
#print(p)
# print('-'*40)

# this is as expected
# it starts with -2, can't get to -5, so there are no elements 
# to be deleted. So the new list is inserted at position -2
p=['a','b','c']
p[-2:-5]=['d','e','f']
# print(p)
# print('-'*40)

# since the whole list lies in the range of indices specified
# it gets overwritten entirely
p=list(range(10))
p[-100:100] = [1]
# print(p)
# print('-'*40)

# positive and negative step and start and stop for selection
# for positive step defaults for start,end are 0,len(list)
p=list(range(10))
a=p[::1]
#print(a)
# print('-'*40)

# for negative step defaults for start,end are -1 and -len(list)-1
p=list(range(10))
a=p[::-1]
#print(a)
# print('-'*40)

# here,we're mixing +ve and -ve indices. convert 4 to -ve notation 
# or the default argument to positive notation
# basically, both indices __have__ to be same sign 
# and you must be able to go from start to end using the step providd
a=p[4::-1]
#print(a)
#print('-'*40)
a=p[:-2:-1]
#print(a)
#print('-'*40)

# finally, the slice operator makes a shallow copy of the list
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

ll1=[l1,l2,l3]
ll2=ll1[0:2]
#print(ll2)
l1.append('a')
#print(ll2)


#finally how does the following assignment work
# step 1: convert -3 to positive index i.e. 5
# step 2: list from 5 to 4 with a step of 1 is empty
#         therefore there are no deletions
# step 3: 'a' is inserted at location -3 (5) and other elements are bumped ahead 
p=list(range(8))
p[-3:4:1]='a'
 