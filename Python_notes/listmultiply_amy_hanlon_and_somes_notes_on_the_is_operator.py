# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:53:38 2020

@author: Gokhale
"""

'''
This is from Amy Hanlon's talk: https://www.youtube.com/watch?v=sH4XF6pKKmk
Relevant location in the talk starts at at time: 8:41.
'''
row   = [""]*3  

'''
    this yields row = ["","",""]
    notice id(row[0]) == id(row[1]) == id(row[2])

what happend?

    [""]*3 returned a list containing three separate objects row[0],row[1],row[2]
    all pointing to the same location because the immutable string is the same
    the interpreter/byte code compiler is smart enough to do this

as an aside:
    
    aa = 1727
    bb = 1727
    aa is bb 
    
    yields False on the interpreter, but True inside a module/file.
    This is because the interpreter/compiler does not make optimizations
    to see that the two 1727s are the same immutable integer. 
    In a file the optimizations occur and hence aa is bb yields True
    
    Similarly for tuples
    aa = (1132,20987,359823)
    bb = (1132,20987,359823)
    yields False on the interpreter, but True inside a module/file.
    
    However, if we use numbers between -5 and 256, these are cached
    by the interpreter (the range is implementation dependent) so
    
    aa = 11 
    bb = 11
    aa is bb 
    
    makes aa and bb point to the same cached integer object and therefore 
    returns True both in a module/file and the interpreter
    
    aa = ["eggs","bacon"]
    bb = ["eggs","bacon"]
    
    aa is bb 
    
    yields False both in interpreter and file/module. 
    This is because new objects are created for mutables
    
    However, since the interpreter/bytecode compiler is smart
    aa[0] is bb[0] yields True in both interpreter/byte code compiler and 
    aa[1] is bb[1] yields True in both interpreter/byte code compiler,
    subject to the same caveats on cacheing and interpreter smartness as 
    before
    
'''

board = [row]*3

'''
    similar to what happened before this creates a list of three objects
    board[0],board[1] and board[2] each of which point to the start
    of object row=["","",""]
    so board[0][ii] is the same object as board[1][ii] which is 
    the same object as board[2][ii] which is the same object as 
    row[ii] for ii \in 0,1,2 i.e. Since they are the same object, they 
    point to the same thing
    
    One can check
    
    id(board[0][ii]) == id(board[1][ii]) == id(board[2][ii]) ==id(row[ii])
    
'''

for ii in range(0,3):
    print(id(board[0][ii]) == id(board[1][ii]) == id(board[2][ii]) ==id(row[ii]))

'''
    So now setting
'''

board[0][1]="W"
    
'''
     Makes the object board[0][1] point to a newly created object "W"
     But board[0][1] is the same object as board[1][1] which is the
     same object as board[2][1] which is the same object as row[1]
    
'''

print(board)
print(row)

'''
    board becomes [['', 'W', ''], ['', 'W', ''], ['', 'W', '']]
    row becomes ['', 'W', '']

finally,

    del row
        
    seems to delete the object row but not clear the contents of the memory
    pointed to by the object row
    
    board 
    
    still is [['', 'W', ''], ['', 'W', ''], ['', 'W', '']]
    
'''
'''
    if one does
    
    row=[1, 2, 3]
    bigrow=row*3  
    
    notice we did not do: bigrow=[row]*3
    
    this yields, bigrow=[1,2,3,1,2,3,1,2,3]
    if we, now mutate row
    row.append(4)
    
    this yields, row=[1,2,3,4], bigrow=[1,2,3,1,2,3,1,2,3]
    
    notice bigrow doesn't change as one might expect from 
    the previous examples
    
    this seems to be because the multiplication operation
    looks inside the first [] and makes three objects which
    point to what is inside the first []. When we use 
    bigrow = row*3 we're actually doing bigrow=[1,2,3]*3
    what is inside the first [] are immutables. But when we do
    bigrow=[row]*3, what is inside the first [] is a mutable list,
    row.
    
    Now let's do:  row=[[1],2,3], bigrow=row*3
    We get bigrow=[[1],2,3,[1],2,3,[1],2,3]
    But now the 1st,4th,and 7th element of bigrow is a mutable
    It points to where the first element of row points. 
    We can mutate that element by doing
    
    row[0].append(4) 
    
    we will get
    
    row=[[1,4],2,3],
    bigrow=[[1, 4], 2, 3, [1, 4], 2, 3, [1, 4], 2, 3]
    
    If we mutate row 
    
    row.append(4) we get
    row=[[1, 4], 2, 3, 4]
    bigrow=[[1, 4], 2, 3, [1, 4], 2, 3, [1, 4], 2, 3]
    
    because, objects inside bigrow were pointing to 
    where where objects inside row were pointing. 
    Bigrow was never pointing to row. 
    
'''

