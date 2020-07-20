# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:49:45 2020

@author: Gokhale
"""

xx = 111

def myfunc(xx=222):
    print("xx inside myfunc=",xx)
    
def changexx(xx):
    xx = 444
    print("xx inside changexx=",xx)
    
def myfunc2(xx=222):
    global xx
    print("xx inside myfunc2=",xx)

#prints 222, prints xx in the local/function namespace
myfunc()   
#prints 111 from the global namespace
print("xx outside myfunc=",xx) 

#prints 333, prints xx in the local/function namespace
myfunc(333)
#prints 111 from the global namespace
print("xx outside myfunc=",xx)

#prints 111. 
#xx in the local/function points to the same place
#as xx in the global namespace
myfunc(xx)
#prints 111
print("xx outside myfunc=",xx)

#prints 444
# xx in the local namespace points to same place
# as xx in the global namespace
# but when xx = 444 is executed, a new object 444
# is created and the local xx points to it
changexx(xx)
# the global xx continues to point to 111
print("xx outside myfunc=",xx)

# the following lines yield
#    global xx
#    ^
# SyntaxError: name 'xx' is parameter and global
myfunc2()
print("xx outside myfunc2=",xx) 

