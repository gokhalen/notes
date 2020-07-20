# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:08:02 2020

@author: Gokhale
"""

from contextlib import contextmanager

class Indenter:
    def __init__(self):
        self.level = 0
        
    def __enter__(self):
        self.level +=1
        return self
        
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.level -=1
        
    def print(self,text):
        print(' '*8*self.level + text)
    
 
class Printer:
    level = -1
    
    def __init__(self):
        self.ll=self.inclevel()
        
    def print(self,text):
        print(' '*8*self.level + text) 
        
    @classmethod
    def inclevel(cls):
        cls.level = cls.level+1
        return cls.level
      
    @classmethod    
    def declevel(cls):
        cls.level = cls.level-1    
    
    
@contextmanager    
def idcongen():
    '''
    yields Printer objects with the appropriate level of indent
    everything before the yield statement is line the __enter__
    method of a class supporting context managers, everything 
    after the yield is like the __exit__ method
    '''
    yield Printer()
    Printer.declevel()
    
with idcongen() as P1:
    P1.print('P1')
    with idcongen() as P2:
        P2.print('P2')
        with idcongen() as P3:
            P3.print('P3')
        with idcongen() as P4:
            P4.print('P4')
    with idcongen() as P5:
        P5.print('P5')

with Indenter() as indent1:
    indent1.print('indent1')
    with indent1 as indent2:
        # indent1's __enter__ method gets called and indent2 refers to the 
        # resulting object returned. Note you can also directly use indent1
        # because indent1's state is altered by the __enter__ call
        indent1.print('indent2')
        

indent1.print('indent1')
