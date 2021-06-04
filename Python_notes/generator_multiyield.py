# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:22:44 2021
@author: aa
"""

def gen():
    a = yield 1
    print(a)
    b = yield 2
    print(b)
    return 1

def gen_mult():
    a = 1
    b = 2
    yield (yield a) + (yield b)
    
    
gg = gen_mult()

# yields a
print(gg.send(None))
# puts 'nachiket' in-place of yield a and executes the next 
# yield (yield b)
print(gg.send('Nachiket'))
# puts ' Gokhale' in place of yield b and executes the next yield
# yield 'Nachiket' + 'Gokhale'
print(gg.send(' Gokhale'))

