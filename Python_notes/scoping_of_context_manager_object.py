# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:35:01 2021

@author: User
"""

with open('temp.out','wt') as fout:
    fout.write('Hello')
    
# fout exists after with block terminates!    
print(type(fout))