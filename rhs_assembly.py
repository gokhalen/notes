'''
Nachiket Gokhale gokhalen@gmail.com

This file shows how to use inheritance, and operator overloading to assemble rhs vectors in FEM.

'''

class Vector():
    '''
    Defines a vector (1-d array) with n-components
    The components are stored in a list
    0 based indexing
    '''
    def __init__(self,n):
        '''
        creates a zero vector of length n
        '''
        self.v = []
        for i in range(n):
            self.v.append(0)

    def __getitem__(self,key):
        # enables getting items using v[key]
        return self.v[key]

    def __setitem__(self,key,value):
        # enables setting items using v[value]
        self.v[key]=value

    def __str__(self):
        s=''
        for comp in self.v:
            s += str(comp) + ' '
        return s


class LocalRhsVector(Vector):
    '''
    we want all the functionality of Vector, plus some additional functionality
    '''

    

v1 = Vector(10)
print(v1)
        
