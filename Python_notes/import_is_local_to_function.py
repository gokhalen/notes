# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:56:38 2020

@author: Gokhale
"""


def printsys():
    import sys
    sys.stdout.write('printsys')
    

def printsys2():
    sys.stdout.write('printsys2')

# prints 
printsys()
# error
printsys2()