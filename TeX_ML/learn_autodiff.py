# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:06:10 2021

@author: User
"""

# Autodiff program
# for straight composition of functions
# output = h(f(g(x)))

import numpy as np

class Node():
    #############################
    # these are nodes in the function graph
    # each node contains a func,
    # list of parents and children
    # for now we assume that we have only
    # one child and one parents
    # input nodes have no parents
    # output nodes have no children
    
    def __init__(self,func_type,parent,name):
        self.func   = Func(func_type)
        
        self.parent = parent
        self.child  = None
        
        self.input  = None
        self.output = None
        
        # if we have a parent set ourself to be that parents child
        if self.parent is not None:
            self.parent.child = self
            
        self.name = name
    
    def __str__(self):
        str1 = f'{self.name}.input = {self.input} '
        str2 = f'{self.name}.output = {self.output}'
        return str1+str2

    
class Func():
    # this is class which provides functions 
    # and derivatives
    func_types = ['linear','quad','sin','cos']
   
    def __init__(self,func_type):
        if func_type not in Func.func_types:
            raise ValueError(f'Unknown function type {func_type}')
            
        self.func_type = func_type
    
    def func(self,xx):
        # this is the function that is computed
        if self.func_type == 'quad':
            return xx*xx
        
        if self.func_type=='sin':
            return np.sin(xx)
    
    def grad(self,xx):
        # this is its gradient of the output with respect to the input
        # evaluated at the input
        if self.func_type == 'quad':
            return 2*xx
        
        if self.func_type == 'sin':
            return np.cos(xx)
            
            
def walk_forward(node):
    # traverse the node from left to right
    node_ = node
    while True:
        yield node_
        if node_.child is not None:
            node_ = node_.child
        else:
            break
        
def walk_backward(node):
    node_ = node
    while True:
        yield node_
        if node_.parent is not None:
            node_ = node_.parent
        else:
            break
        
def forward_pass(node):
    walker = walk_forward(node)
    for node in walker:
        node.output = node.func.func(node.input)
        if node.child is not None:
            node.child.input = node.output
        # print input and output
        print(node)
        
def backward_pass(node):
    walker = walk_backward(node)
    gradient = 1.0
    for node in walker:
        _grad = node.func.grad(node.input)
        gradient *= _grad
 
    return gradient
        
'''
# input x, output = x^16
node1 = Node('quad',parent=None,name='input')
node2 = Node('quad',parent=node1,name='hidden1')
node3 = Node('quad',parent=node2,name='hidden2')
node4 = Node('quad',parent=node3,name='output')
node1.input = 2
forward_pass(node1)
gradient=backward_pass(node4)
gradient_true = 16*(node1.input**15)
'''


# input x, output (sin(x))^2
node1 = Node('sin',parent=None,name='input')
node2 = Node('quad',parent=node1,name='output')
node1.input = 2
forward_pass(node1)
gradient=backward_pass(node2)
gradient_true=2*np.sin(node1.input)*np.cos(node1.input)

print(f'{gradient_true=},{gradient=}')
