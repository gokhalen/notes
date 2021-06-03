# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:44:15 2021

@author: aa

"""
# can't have two * argument types
# because Python does not know how to divide the arguments 
# between args1 and args2
#def ff(*args1,*args2):
#    print(args1,args2)

# can't have two ** argument types
# similar reasons as above
# def ff(**kwargs1,**kwargs2):
#    print(kwargs1,kwargs2)

# does not like * following **
# def ff(**kwargs,*args):
#    print('hello')

# allowed
#def ff(*args,**kwargs):
#    print('hello')

# this is allowd, but named1 has to be a keyword argument
def ff(*args,named1,**kwargs):
    print(args)
    print(named1)
    print(kwargs)

# not allowed because there is no named1=     
# ff(1,2,john=1)

ff(1,2,named1='paul',john=1,kambli=2)
