'''
Mostly based on python-course.eu Properties Vs Gettors by Bernd Klein
'''
class P1:
    '''
private variable xx and setter and getter methods
problem is that this leads to expressions like  
p1.set_x(p1.get_x()+p2.get_x())
    '''    
    def __init__(self,xx):
        self.__xx = xx
        
    def get_xx(self):
        return self.__xx

    def set_xx(self,xx):
        self.__xx = xx


class P2:
    '''
rewrite the class in a pythonic way
instead of the attribute self.__x we use a public attribute
but there is no data encapsulation here
But what happens if we want to change the implementation in the future. This is a serious argument. Let's assume we want to change the implementation like this: The attribute x can have values between 0 and 1000
    '''
    def __init__(self,xx):
        self.xx = xx


class P3:
    '''
this class includes methods to check the value of xx before setting it
we have also made xx private
this will break code which we have written below:
    p1.xx = 100
    '''
    def __init__(self,xx):
        self.set_xx(xx)

    def get_xx(self):
        return self.__xx

    def set_xx(self,xx):
        if xx < 0:
            self.__xx = 0
        elif xx > 1000:
            self.__xx = 1000
        else:
            self.__xx = xx

class P4:
    '''
we make xx public again and define setter and getter methods via properties
disadvantage: xx is public
advantage we can write code like p1.xx=15 and run it through the setter automatically 
    '''
    def __init__(self,xx):
        self.xx = xx

    @property
    def xx(self):
        print("Calling Getter")
        return self.__xx  #note the __xx, even though xx is public

    @xx.setter
    def xx(self,xx):
        print("Calling Setter")
        if xx < 0:
            self.__xx = 0
        elif xx > 1000:
            self.__xx = 1000
        else:
            self.__xx = xx


class P5:
    '''
       this is another way to achieve the same effect as P4
       xx is still public
       P4 is more pythonic
    '''
    def __init__(self,xx):
        self.set_xx(xx)

    def get_xx(self):
        return self.__xx  #note the __xx, even though xx is public
    
    def set_xx(self,xx):
        if xx < 0:
            self.__xx = 0
        elif xx > 1000:
            self.__xx = 1000
        else:
            self.__xx = xx
            
    xx = property(get_xx,set_xx)

'''
there is a problem with P4 and P5. We can do both: 
pp = P4(42)
pp.xx = 11  or pp.set_xx(42)
pp.xx       or pp.get_xx()
This way we are violating one of the fundamentals of Python: "There should be one -- and preferably only one way to do it
we can fix this problem by making the getter and setter methods private, which can't be accessed outside the class

'''
class P6:
    '''
       this turns the setter and getter methods in P5 into private methods. xx is still public
    '''
    def __init__(self,xx):
        self.__set_xx(xx)

    def __get_xx(self):
        return self.__xx  #note the __xx, even though xx is public
    
    def __set_xx(self,xx):
        if xx < 0:
            self.__xx = 0
        elif xx > 1000:
            self.__xx = 1000
        else:
            self.__xx = xx
            
    xx = property(__get_xx,__set_xx)

'''
now, can we make a pythonic version of P6? i.e. P4 with private setters and getters
'''



class P7:
    '''
       emulates a private variable with public mutators
       this is based on bryanrunck.com
    '''
    
    def __init__(self,xx):
        self.xx = xx
        
    @property    
    def xx(self):
        print("Calling getter")
        return self.__xx

    @xx.setter
    def xx(self,xx):
        print("Calling setter")
        if xx < 0:
            self.__xx = 0
        elif xx > 1000:
            self.__xx = 1000
        else:
            self.__xx = xx

class P8:
    
    def __init__(self,xx):
        self.__xx = xx
        
    @property    
    def __xx(self):
        print("Calling getter")
        return self.aa

    @__xx.setter
    def __xx(self,xx):
        print("Calling setter")
        if xx < 0:
            self.aa = 0
        elif xx > 1000:
            self.aa = 1000
        else:
            self.aa = xx

'''
the cases considered so far

P1: private variable, handwritten public setter and getter methods
P2: public  variable, no setter getter methods
P3: private variable, handwritten public getter and setter methods with some checking
P4: public  variable, pythonic public setter and getter functions using @property. 
    But two ways to assign: pp.xx = 1 / pp.set_xx(1) and two ways to get. Not pythonic.
P5: public variable, public setter and getter using property(,), which is not pythonic. 
P6: public variable, private setter and getter using property(,), which is not pythonic
P7: private variable, public setter and getter using @property, which is pythonic.
    This emulates a private variable. when one calls pp.xx=10, method xx.setter is called and 
    10 is stored in self.__xx. When one gets pp.xx as in aa = 2*pp.xx the @property is called

There is not much difference between P4 and P7. When you call pp.xx=value python calls 
the mutator. When you do aa=pp.xx*2, python calls the accessor. Since our calls are going 
through the mutator and accessor, it really doesn't matter how the variable is stored inside
(whether public or private) or whether the mutators and acessors are public or private.
One can always make a mockery of encapsulation by accessing the mangled variables.

Look at class P8. The names of the mutator methods will be mangled. pp.__xx will
say that object has no attribute __xx. They can still be called
through their mangled names. Because of mangling, it is not a good idea to write private 
mutator names.

  
'''

pp = P4(42)
