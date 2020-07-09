'''
Nachiket Gokhale gokhalen@gmail.com

This file shows how to use inheritance, and operator overloading to assemble rhs vectors in FEM.

'''

import typing

class Vector():
    '''
    Defines a vector (1-d array) with n-components
    The components are stored in a list
    0 based indexing
    '''
    def __init__(self,n:int=None,ll:list=None):
        '''
        If ll is None:
        	1) If n is None an exception is is thrown
        	2) if n is specified, then a zero vector of length n is created
        3) If ll is specified and non-empty:
        	1) n is ignored and a vector of length len(ll) with the contents of ll is created
        '''
        self.v = []
        if ( ll == None ):
            if ( n== None ):
                raise RunTimeError('Both n and ll undefined in class Vector')
            else:
                for i in range(n):
                    self.v.append(0)
        else:
            self.v = ll

    def __getitem__(self,key):
        # enables getting items using v[key]
        return self.v[key]

    def __setitem__(self,key,value):
        # enables setting items using v[value]
        self.v[key]=value

    def __iter__(self):
        self.positer = 0
        return self

    def __next__(self):
        if (self.positer < len(self.v)):
            result = self.v[self.positer]
            self.positer += 1
            return result
        else:
            raise StopIteration('Iterator exhausted in Vector')

    def __str__(self):
        s=''
        for comp in self.v:
            s += str(comp) + ' '
        return s



class LocalRhsVector(Vector):
    '''
    we want all the functionality of Vector, plus some additional functionality,
    namely, a vector which contains information on where the local dofs go in
    the global element vector. Therefore, we inherit from Vector
    '''

    def __init__(self,n,l2gmap):
        # we're inheriting
        super().__init__(n)
        self.l2gmap = Vector(None,l2gmap)

class GlobalRhsVector(Vector):
    
    def __init__(self,n):
        super().__init__(n)

    # overload the += operator
    def __iadd__(self,v:LocalRhsVector):
        for value,glbloc in zip(v,v.l2gmap):
            print('value=',value,'glbloc=',glbloc,'self.v[glbloc]=',self.v[glbloc])
            self.v[glbloc] += value

        return self
    
# just a base class object for debugging purposes
vbase      = Vector(10)

# define a LocalRhsVector
l2gmap       = [0,9]
vlocalrhs    = LocalRhsVector(2,l2gmap)
vlocalrhs[0] = 2.718
vlocalrhs[1] = 1.414 
# define a GlobalRhsVector
vglobalrhs = GlobalRhsVector(10)
print(vglobalrhs)
vglobalrhs += vlocalrhs
print(vglobalrhs)


         

        
