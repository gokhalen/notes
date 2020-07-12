# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# [1] https://stackoverflow.com/q/19892204/13560598
# [2] https://hackernoon.com/python-generators-35ac68334882

# f.s. = following statement

def coro():
    print('before yield')
    a = yield 'the yield value'
    b = yield a 
    print ('done!')

c=coro()

# from [1]
# You can't send() a value the first time because the generator did not
# execute until the point where you have the yield statement, so there is
# nothing to do with the value.

# advance the generator to the first yield and yield 'the yield value'
print(next(c))
# the assignment to a hasn't happened yet, 'the yield value' was yielded
# and the code is waiting for the assignment to a to happen
# the following code causes the assignment to occur,
# goes to the next statement where it yields 'John' and waits for 
# assignment to b to happen
print(c.send('John'))
# this statement causes assignment to be to happen, 
# and goes to the next yield statement (which does not exist)
# returns NONE and thus StopIteration is raised
try:
    print(c.send('Paul'))
except StopIteration as e:
    print('StopIteration was raised. Code would have terminated here if not handled')
print('-'*100)

def whizbang():
    for i in range(10):
        x = yield i
        print (f'I got {x}')

wb = whizbang()

# f.s. yields 0 and waits for assignment to x to happen
print(next(wb))
# f.s. sets the value of x to 'John' and loops until it hits a yield statement
# it yields the value 1, and waits for assigment to happen
print(wb.send('John'))
# f.s. sets the value of x to 'Paul' and loops until it hits a yield statement
# it yields the value 2, and waits for assigment to happen via next send
print(wb.send('Paul'))
# and so on and so forth
print('-'*100)

# if there is no expression/object on the LHS to receive the value sent
# by 'send', that value is 'lost' 
def lostvals():
    yield 1
    yield 2
    yield 3
    
lv = lostvals()

# yields 1
print(next(lv))

# assigns 'a' to an unnamed/non-existing variable  of the lhs of yield 1
# goes to the next yield to yield '2' and waits for assignment to occur to 
# the left of yield 2
print(lv.send('a'))

# assigns 'b' to an unnamed/non-existing variable  of the lhs of yield 2
# goes to the next yield to yield '3' and waits for assignment to occur to 
# the left of yield 3
print(lv.send('b'))

# StopIteration raised because the function 'returns'
# When no return statement is there, a function returns None
try:
    print(lv.send('c'))
except StopIteration as e:
    print('StopIteration was raised in lostvals')

print('-'*100)


# a concrete example
def stepgen(start,step):
    state = start
    while True:
        newstep = yield state
        if (newstep != None ):
           step = newstep
        state = state + step
        
# start the step generator
sg = stepgen(0,1)
print(next(sg))
print(next(sg))
# can change the step on the fly
# when you do next(sg) you are sending None
# you can check for that and decide whether to change step 
# or not
print(sg.send(4))
print(sg.send(5))        
