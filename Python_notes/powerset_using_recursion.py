# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 18:40:39 2021

@author: User
"""
import numpy as np
import itertools
import functools

# @functools.lru_cache(1024)
# apparently functools does not work when input is a set
# args need to be hashable it seems
def powerset(setin):
    # returns a set containing tuples
    # return  if set containing an empty tuple
    # set that will be returned
    
    outset = set()
    if setin == {()}:
        # .add ensures uniquness of set elements
        outset.add(())
    else:
        # setin contains only one tuple but we cannot access it by indexes
        # because sets are not ordered
        for tup in setin:
            # add the input set to  the output
            # .add ensures uniqueness
            outset.add(tup)
            tuplen = len(tup)
            tuples = tuple(itertools.combinations(tup,tuplen-1))
            
        for tup in tuples:
            ss = powerset({tup})
            # ss contains many tuples
            for _t in ss:
                outset.add(_t)
    return outset    


    

nn   = 6
# set containing one tuple
tt = tuple(np.arange(nn))
set_ = set((tt,))

ps = powerset(set_)
# print(ps)