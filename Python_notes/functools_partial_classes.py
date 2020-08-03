# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:40:24 2020

@author: aa
"""
import functools

class Base():
    def ff(self,x=1,y=2,z=3):
        return (x,y,z)
    


bb = Base()
print(bb.ff(101,202,303))
print(bb.ff1(y=202,x=303))