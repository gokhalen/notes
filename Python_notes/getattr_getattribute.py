# ***********************************************
# RUN THIS ON THE COMMAND LINE, NOT IN SPYDER
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute
# https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute/3278104#3278104
# https://python-reference.readthedocs.io/en/latest/docs/dunderattr/getattribute.html
# ************************************************
# __getattribute__ is always called first. 
# If it raises an AttributeError then getattr is called
# from python-reference above:
# If the class also defines __getattr__(), the latter will not be called unless __getattribute__() either calls it explicitly or raises an AttributeError.
# In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example,
# >>> object.__getattribute__(self, name).
# As Mad Physicist says in the second Stack link:
# objec.__getattribute__ invokes myclass.__getattr__ under the right circumstances


import sys


class AA:
    def __init__(self,dd,student_id):
        # sets a dictionary
        self.student_id = student_id
        self._dd  = dd
        
    def __getattr__(self,name):
        print('__getattr called__')
        try:
            return self._dd[name]
        except KeyError:
            return 3.14

dd = {'j':1,'p':2,'g':3,'r':4}        
aa = AA(dd,1024)

# getattr is not called because student_id 
# is a real attribute
print(aa.student_id)

# j,p,g,r are not real attributes
# they are faked. when attributes are not found
# getattr is called as a backup
print(aa.j)
print(aa.p)
print(aa.g)
print(aa.r) 
print(aa.pq)
print('-'*80)
#################################################################################
class BB():
    def __init__(self,dd,student_id):
        self.student_id=student_id
        self._dd=dd
        
    def __getattr__(self,name):
        print('__getattr called__')
        try:
            # if __getattr__ is called in response to AttributeError
            # raised by __getatrribute__
            # the following will lead to an infinite recursion
            # because accessing attributes calls getattribute which
            # calls getattr and which calls getattribute and so on
            # e.g. the following calls will not work
            # return self.__dict__['student']
            # self.student
            print('returning from __getattr__')
            value =  self._dd[name]  # this makes another call to __getattribute__
            print('__getattr__ computed return value')
            return value
        except KeyError as e:
            raise AttributeError('Key not found in __getattr__') from e
        
        
    def __getattribute__(self,name):
        # get attribute is called before getattr for every call
        print('__getattribute__ called')
        
        # if AttributeError is raised, __getattr__ will be called
        # if in response, __getattr__ tries to access any variable
        # using the . notation, there will be a infinite recursion
        # raise AttributeError
        
        # raise AttributeError('Attribute Error in __getattribute__')
        
        # if the following is called, the __getattr__ handles
        # everything like magic, no infinite recursions
        return super(BB,self).__getattribute__(name)
        #return self.__dict__[name]
        
bb = BB(dd,2048)
# getattr is not called because student_id 
# is a real attribute
print(bb.student_id)

# j,p,g,r are not real attributes
# they are faked. when attributes are not found
# getattr is called as a backup
print(bb.j)
print(bb.p)
print(bb.g)
print(bb.r) 
