# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:11:45 2020

@author: Gokhale
"""

aa = 1727
bb = 1727
# this will yield False in the Interpreter and True in file/module
# because the interpreter is not smart enough to recognize that 
# the two 1727's are actually the same object
# the Compiler is smart enough to recognize  
print(aa is bb)  

aa = (1132,20987,359823)
bb = (1132,20987,359823)
print(aa is bb)

aa = (11,20,35);
bb = (11,20,35);
print(aa is bb)

aa = ["eggs", "bacon"]
bb = ["eggs", "bacon"]
print(aa is bb)               #False
print(aa[0] is bb[0])         #True
print(aa[1] is bb[1])         #True