# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:02:00 2021

@author: aa
"""

import functools,types

# Fibonacci program using yields 
# Inspired by Python Cookbook - Beazley Jones 2013 pg 311

class FibNode():
    def __init__(self,idx):
        # initialize self
        self.idx   = idx 
        self.value = None
        # left child is idx-1, right child is idx-2
        self.left  = self.create_child(idx-1)
        self.right = self.create_child(idx-2)
            
    def __str__(self):
        return f'(idx={self.idx},value={self.value})'
    
    
    def create_child(self,idx):
        if (idx >1):
            return FibNode(idx)
        else:
            _child       = FibNode.__new__(FibNode)
            _child.idx   = idx
            _child.value = idx
            _child.left  = None
            _child.right = None
            return _child
    
    def children(self):
        _children = []
        if ( self.right is not None):
            _children.append(self.left)
            
        if ( self.left is not None):
            _children.append(self.right)
        
        return _children
        
    def printbfs(self):
        _list = [[self]]
        for _levellist in _list:
            print('-'*80)
            # children at the level below
            _children = []
            for _nd in _levellist:
                # print the node
                print(_nd)
                # append its children to the list
                _nd_childs = _nd.children()
                if (_nd_childs):
                    _children.extend(_nd_childs)
            if (_children):            
                _list.append(_children) 
            print('-'*80)
            
            
    def fibgen(self):
         leftyield  = self.left.fibgen()  if self.left.value  is None else self.left.value
         rightyield = self.right.fibgen() if self.right.value is None else self.right.value
         yield (yield leftyield) + (yield rightyield)
            
          
            
# for testing purposes
@functools.lru_cache
def fibrecurcache(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    
    return fibrecur(n-1) + fibrecur(n-2)


def fibrecur(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    
    return fibrecur(n-1) + fibrecur(n-2)

            
class FibEval():
    '''
    Starts with top node of a Fibonacci tree defined above by FibNode
    And yields things
    '''
    def fibeval(self,fibnode):
        stack       = [fibnode.fibgen()]
        last_result = None
        while stack:
            # print(f'{stack=}')
            try:
                last = stack[-1]
                if isinstance(last,types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result=None
                else:
                    last_result=stack.pop()
                    
            except StopIteration:
                # remove the genrator from the stack
                stack.pop()
        
        return last_result
        

def fibyield(nn):
    ff=FibNode(nn)
    # ff.printbfs()
    evaluator = FibEval()
    evaluator.fibeval(ff)
        
if __name__=='__main__':
    fibyield(10)