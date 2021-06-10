# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:11:10 2021

@author: aa
"""
# Python Cookbook, p.g. 385  Beazley Jones

class list_man():
    def __init__(self,orig_list):
        # make a copy of the original list
        self._orig_list = orig_list
        # keep a reference to the original list
        self.working = list(orig_list)
    def __enter__(self):
        print('starting context ...')
        # return an object we can work with
        return self.working
    def __exit__(self,exc_ty,exc_val,exc_tb):
        # if no exceptions were raised, modify the original list
        # through the reference
        print('exiting context....')
        print(f'{exc_ty=},{exc_val=},{exc_tb=}')
        if not exc_ty:
            self._orig_list[:] = self.working

ll = [1,2,3,4]
with list_man(ll) as lcon:
    lcon.append(5)
    lcon.append(6)
    # if exceptions were raised the original list is not modified
    # raise RuntimeError('Runtime Error')