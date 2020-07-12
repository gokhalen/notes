'''
https://dabeaz-course.github.io/practical-python/Notes/05_Object_model/02_Classes_encapsulation.html
When you use __slots__, Python uses a more efficient internal representation of objects
It should be noted that __slots__ is most commonly used as an optimization on classes that serve as data structures. Using slots will make such programs use far-less memory and run a bit faster.
'''

class Pizza(object):
    __slots__ = ['xx']
    def __init__(self):
        self.xx = 1

        

marg = Pizza()
sicilian = Pizza()
# not allowed to add a new variable yy
marg.yy = 2
# but you can still add a new class variable
# marg.__class__.xx = 2