# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:28:56 2020

@author: Gokhale
"""

aa = [0,1,2,3,4,5,6,7,8,9]

aa[2:4] = [10,11,12]

'''
This means remove elements from 2:4 (not including the element at index 4),
and insert element of the sequence at index 2 and expand or contract the 
list 

this yields 

aa = [0, 1, 10, 11, 12, 4, 5, 6, 7, 8, 9]

2,3 have been removed from the original list
[10,11,12] have been inserted starting at index 2

'''

aa = [0,1,2,3,4,5,6,7,8,9]
aa[2:8] = [10,11,12]

'''
removes elements indexed from 2 to 7 (last number is not included)
and inserts the sequence [10,11,12] at index 2. The above yields,

aa=[0, 1, 10, 11, 12, 8, 9]

'''