# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:30:27 2020

@author: aa
"""


def sdir(obj,ss):
    # obj : object supporting dir()
    # ss  : Iterable yielding strings to search in dir
    return [ llword for llword in dir(obj) for word in ss if word in llword]
    