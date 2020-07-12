class Pizza(object):
    __isfrozen = False
    def __setattr__(self,key,value):
        if self.__isfrozen and not hasattr(self,key):
            raise TypeError("%r is a frozen class" %self)
        object.__setattr__(self,key,value)

    def freeze(self):
        self.__isfrozen = True

    def __init__(self):
        self.radius = 10
        self.meat   = "Chicken"


class Pasta(object):
    __yy = 314
    yy = 271
    
    def __init__(self):
        print ("Calling __init__")
        self.xx = 2
        
    def __repr__(self):
        return f'yy={self.yy!r},__yy={self.__yy!r}'
        
Alfredo = Pasta()

#marg = Pizza()
#sicilian = Pizza()
#marg.yy = 2
#sicilian.yy = 

#print("marg.yy = ",marg.yy)
#print("sici.yy = ",sicilian.yy)
