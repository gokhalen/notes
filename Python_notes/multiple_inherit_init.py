# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:00:29 2020
@author: Gokhale

Constructor order in multiple inheritance is complicated
This example shows the right way to do it.
D is a child of (A,B,C)
Leaving out super calls in the parent classes causes problems
"""



class A(object):
    def __init__(self):
        print("Entering __init__ A")
        super(A,self).__init__()
        print("Leaving __init___ A")

class B(object):
    def __init__(self):
        print("Entering __init__ B")
        super(B,self).__init__()
        print("Leaving __init___ B")

class C(object):
    def __init__(self):
        print("Entering __init__ C")
        super(C,self).__init__()
        print("Leaving __init___ C")

class D(A,B,C):
    def __init__(self):
        print("Entering __init__ D")
        super(D,self).__init__()
        print("Leaving __init___ D")
        
    def __nachiket__(self):
        print('nachiket')
        
dd = D()
dd.__nachiket__()