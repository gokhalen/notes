# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:44:50 2020

@author: Gokhale
"""

def countdown(n):
    while n > 0:    
        yield n
        n -=1
        
if __name__ =='__main__':

# this prints 10,9,8..5, not 10,10,10,10,10 
# i.e. a new countdown object/function is not created everytime within 
# the same for loop. that would be self defeating
    for ii in countdown(10):
        print(ii)
        if ii == 5:
            break
        
    print(f'{"-"*25}')  
        
# this restarts the countdown from 10 
# a new countdown generator is created at the start of the loop       
    for ii in countdown(10):
        print(ii)
        
    print(f'{"-"*25}')  
        
    gg = countdown(10)
# this prints 10,9,8,7,6,5
    for ii in gg:
      print(ii)
      if ii == 5:
          break
      
    print(f'{"-"*25}')  
# this restarts where the last one left off
# this prints 4,3,2,1
    for ii in gg:
      print(ii)  

    print(f'{"-"*25}')  

# this does not print anything - the generator is exhausted  
# if you want to restart, create a new generator using gg=countdown(10) 
    for ii in gg:
        print(ii)

    print(f'{"-"*25}')  
    
    gg = countdown(10)
    for ii in gg:
        print(ii)
