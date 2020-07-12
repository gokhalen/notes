# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Student:
    # class variable
    school="Karnatak High School"
    
    def __init__(self):
        # examples of calling class, static, and normal methods from within instance
        self.marks=0
        
        self.cls_setschool('VIT')
        self.stat_setschool()
        self.norm_setmarks(95)
    
    def __str__(self):
        return f'School={self.__class__.school},marks={self.marks}'
    
    @classmethod
    # gets passed the class automatically when called from instance or class
    # from within the class this needs to be called as self.cls_setschool
    def cls_setschool(cls,school):
        cls.school=school
        
 
    @staticmethod
    # does not get passed class or instance automatically
    # from within the class this needs to be called as self.stat_setschool()
    # one can explicitly pass it though
    # can also be called directly from the class without instantiating an object
    def stat_setschool():
        print('@staticmethod stat_school()')
    
    @staticmethod
    # we can explicitly pass a class to a static method
    def stat_method_class(cls):
        print(cls.school)        
    
    @staticmethod
    # we can explicitly pass an object to a static method
    def stat_method_object(self):
        print(self.marks)
 
    # gets passed the instance automatically
    # can be called on an object from a class but needs to be passed the 
    # object explicitly i.e. the self argument needs to be explicitly specified
    def norm_setmarks(self,marks):
        self.marks = marks
        
if __name__ =="__main__":
    # create Student object. 
    s1 = Student()
    print(s1)
    
    
    # In the next few lines, we call methods from the class itself, not instance
    Student.cls_setschool('MIT')
    # we can also do the following. Note, the self argument needs to be
    # explicitly passed, because there may not be a instance defined from the class
    Student.norm_setmarks(s1,99)
    Student.stat_setschool()
    print(s1)
    
        
    # In the next few lines, we call methods from the instance
    # when calling a classmethod from an instance, there is no need to 
    # pass the class because the class already exists
    s1.cls_setschool('Fergusson College')
    s1.norm_setmarks(101)
    s1.stat_setschool()
    print(s1)
    
    # we can explicitly pass classes to staticmethods
    s1.stat_method_class(Student)
    Student.stat_method_class(Student)
    
    # we can explicitly pass objects to staticmethods
    s1.stat_method_object(s1)
    Student.stat_method_object(s1)
    
    # we can also mix the above two patterns and pass both classes and objects
    
