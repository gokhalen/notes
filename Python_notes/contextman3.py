# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:59:05 2020

@author: Gokhale
"""
from contextlib import contextmanager

@contextmanager
def open_file(name):
    # anything upto yield is like the __enter__ method
    # anything after yield is like the __exit__ method
    f = open(name,'w')
    try:
        print('calling try')
        yield f
    finally:
        print(f'closing {name}')
        f.close()
        
with open_file('outfile.txt') as f:
    # f references the object yielded by open_file
    f.write('A!\n')
    f.write('B!\n')
    with f as f2:
    # because of the @contextmanager decorator and language magic
    # we can refer to f as f2. Note 'calling try' is executed only once
    # a new file is not opened
        f2.write('C!\n')
        
    # when we get out of scope of the second "with" the code 
    # equivalent to __exit__ , i.e. the finally block is called
    # the fle is closed
    
    # the following will fail    
    #@f.write('D!\n')
    
    
# this will fail too
# f.write('E\n')
