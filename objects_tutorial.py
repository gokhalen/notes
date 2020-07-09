'''
 Nachiket Gokhale gokhalen@gmail.com

 Since you said twice that you could not wrap your head around objects
 and OOP (Object Oriented Programming) here is my attempt to explain objects to you.
 Perhaps it might teach me a few things too. They say that the best way to learn 
 is to teach. Let me test that out. Some things that I write here are very basic,
 you might already know them. Please forgive me for repeating them.

 1)   What is an object?

 ans)    An object is a 'thing' that contains data and functions to manipulate 
         (perform operations on) that data. An object contains data and methods (functions).
         One can also think of it as a way of organizing data and functions. 
         Objects can also be thought of as a way of keeping data and functions 
         'close' to each other.

         It promotes code re-use (which means less code, so less bugs to fix and therefore
         code becomes more 'maintainable'). We write objects for the same reason we write
         functions: to reduce the amount of code and make it more readable. If we find
         ourselves doing the same thing over and over again, we write a function to do that thing.
         In OOP we go one step further and group together functions and the data on which the 
         functions typically operate. 

         For example, a vector in R^2 can be a thought of as an object. The data it contains are
         its two components. The functions it contains are used to maniputate its data. i.e.
         to define what happens when we add two vectors, or to define 
         what happens when we multiply two vectors

         Another example: A linear elasticity finite element could be thought of as an object. 
         The data it contains could be the list of nodes (in correct order), their coordinates,
         the material properties \lambda and \mu, and functions to build the element stiffness matrix 
         and right hand side. The nodes themselves could be objects. The data in a node object
         could be: the coordinate of that node, the node number. To build the global stiffness
         matrix, you simple go to each element ask it to provide you its local stiffness matrix,
         which you can assemble into the global stiffness matrix. This is pretty much what I did
         in the code I wrote for my Ph.D. 

         A 'class' provides the definition of an object. A 'class' is a factory that produces 
         objects. 

         If I tell you that: x \in R^2 and y \in R^2 you know how to compute x+y,
         x-y, and element-wise product x*y and element-wise division x/y. If I tell you that
         x and y are complex numbers, you know how to compute x+y and x-y because the 
         set of complex numbers defines how to perform addition and subtraction for all
         members of that set. In other words, x and y come with properties, defined by the 
         space they come from which tell you how to perform operations.

         Similarly, when objects are defined from a 'class' or created from a 'class' 
         they come with functions which can do things that the objects are supposed to do. 
 
         In all programming languages I know of, we write:

         'R^2 x' and similarly, 'R^2 y'

         instead of saying x \in R^2, y \in R^2.

         That defines x and y as members of R^2, or in programming terms, the type of x and y
         is R^2. 

         We can also say that x and y are 'instances' of the 'class' R^2. We also say we can 
         'instantiate' R^2 to get x and y.

         An object has 'behaviors' which means we can control how things happen when
         we perform operations on an object. These operations could be applying the operators
         +,-,* and to an object. Defining these operations promotes 'clearer thinking' about 
         the problem at hand.

         For example, if we want to add two vectors v1 and v2 and get a third vector v3, we can
         do this in two ways:

         v3=addvector(v1,v2)         .... here we are using a function to add two vectors
         
         or 

         v3=v1+v2

         Obviously, the second way is better because it is cleaner, more elegant. If we want 
         to add three vectors to get a fourth we can do

         vtemp = addvector(v1,v2)
         v4    = addvector(vtemp,v3)

         or we can just do:

         v4 = v1+v2+v3+v4

         Clearly using the function addvector will quickly get out of hand. 
         Yes, I know we could write a function to accept an arbitrary number of arguments, but

         v4 = v1+v2+v3 is still cleaner and more elegant than v4=addvector(v1,v2,v3) 
         
         Note: v4=v1+v2+v3 needs a compiler/interpreter smart enough to evaluate v1+v2, 
         understand that the result is a vector, create that temporary vector v1+v2 and then add
         v3 to it. But this is the domain of compiler engineers and I know nothing more 
         of this.  

******************************************************************************************************************
                                         ____IMPORTANT____
*******************************************************************************************************************
         
         Everything in Python is an object. The number 1 is an object. It is an instance of class 'int'.
         The number 2.7 is an object. It is an instance of class 'float'. Even functions are objects.
         Functions are instances of the class 'function'.

         Let's look at the following code.

         a=1 
         
         In Fortran (f77) or C, this means go to the memory location allocated for the variable 'a' and write '1' there. 
         This is not the way things work in Python. A better way to say it would be: this is not a good mental model 
         for how Python works. In Python, the statement 'a=1' means: 'a' is another name for the object '1'.  Or you 
         can say: 'a' is an alias for the object '1'. Or you can say: 'a' points to '1'. 

         Now look at the following code:

         a=1
         b=a
         c=b

         Python looks at the first statement, says 'a' is a name/label for '1'. Then 'b=a' means 'b' is another name/label for 'a'.
         But Python knows that 'a' is another name/label for '1'. So it draws the conclusion that 'b' is another name/label for '1'.
         Similarly, it draws the conclusion that 'c' is another name/label for '1'. Variables are nothing but labels/names for objects.

         If you really want to take the object (data and methods) that are labelled 'a' and make a separate copy in memory, and have that 
         copy labelled 'b' you have to do it explicitly. I won't say how, it will distract from the main issue which is learning 
         about objects. 

         Now look at the following code:

         a=5
         b=3
         c=a+b
         
         The first line creates an object '5' and assigns the label/name 'a' to it. The second line creates an object '3'
         and assigns the label/name 'b' to it. Notice that the rhs is evaluated first and the lhs is merely a label for it. 
         Similarly for the third line 'c=a+b', the objects labelled 'a' and 'b' are added, a new object '8' is created and 
         'c' is merely a label for that new object. How are 'a' and 'b' added? They have methods which tell you how they are added.   


         
So, let's start. 

Use Python 3.7 or better. Put 'breakpoint()' where you want to stop the code and get a debugger prompt. You
should be able to perform various Python operations at the debugger prompt. Use 'continue' or 'c' to proceed. You can also define 
variables at the debugger prompt. Make sure that your variable names do not conflict with debugger commands. So, writing 'b=2'
on the debugger prompt is not a good idea, because 'b' is a debugger command which sets breakpoints. 'b=2' will signal to the 
debugger that you're trying to do something with breakpoints. One way to make your variable names not conflict with the debugger 
commands is to start with your initials or some other unique identifier. You might say: peb_b = 2. That should work. Similarly,
'c=2' on the debugger prompt is not a good idea because 'c' means 'continue' to the debugger.

There are many things I haven't covered here. Inheritance, encapsulation, difference between class and instance variables,
classmethods and staticmethods are things which come to mind. 
 
'''

# Let's define a function to add two vectors. I won't define functions to subtract, elementwise multiply and divide
# Defining an excessive number of functions will distract from the goal of learning about objects.

def vector_add(v1,v2):
    '''
    v1 and v2 are lists of length 2
    lists are like 1-d arrays using 'v1[0]' gets the first element, 'v1[1]' gets the second element
    indexing starts at 0

    note: we have not declared the data type for the elements of v1 and v2. they could be integers,floats,
    complex numbers or even strings. As long as the operation '+' is defined for whatever datatype we're passing in
    this code will work. 

    As you can see, we don't need different functions to add different data types. 
    This is a good thing and a bad thing.

    '''
#   add the x components, then the y-components   
    x  = v1[0] + v2[0]
    y  = v1[1] + v2[1]

#   create a list and return it. [x,y] makes a list out of x and y.
    v3 = [x,y]            
    return v3
    
# Let's define two vectors v1 and v2 and get a third v3. Using [] defines a 'list' in Python.
v1 = [1,2]
v2 = [3,4]

v3 = vector_add(v1,v2)

print(v3)

# so, v3 = [4,6] so things are as we expected

breakpoint()

# Let's do the same exercise with classes.
# Lets define a class called Vector
# the keyword class tells the compiler that Vector is a 'factory' for producing objects of the type 'Vector'
# Let's build this class slowly, using the fact that newer definitions of the class override older ones
# the keyword 'pass' is a placeholder, it does nothing.
# so this vector class does nothing, since it has no data and no methods
class Vector():
    pass

# we are creating two objects v1 and v2 from the class
# v1 and v2 are 'instances' of the class Vector
# or Vector is 'instantiated' to get v1 and v2
# Vector() on the rhs creates an object and allocates memory for it.
# the lhs merely names the newly creates object as v1
# equivalently, we can say that v1 points to a new object of type Vector
# we can make similar statements about v2
v1 = Vector()
v2 = Vector()

print('Type of v1 is = ',type(v1))
print('Type of v2 is = ',type(v2))

# so we can see the type of v1 and v2 is <class '__main__.Vector'>
# the __main__ comes up because the class Vector is defined in the main body of the program we're running

v1.x = 1
v1.y = 2

v2.x = 3
v2.y = 4

# what have we done in the above four lines? we have created variables x and y and they're stored inside v1 and v2
# Python goes inside the objects v1 and v2 and create variables named x and y. 
# python is a bit unusual in that it lets you define variables inside v1 and v2 without declaring them first.
# I call this the ability to define variables dynamically
# Other langauges like C++ don't let you do so.
# v1 and v2 have their own copies of x and y.
# x and y are called instance variables
# Let's look at the variables we defined.

print('v1.x= ',v1.x, 'v1.y= ',v1.y)
print('v2.x= ',v2.x, 'v2.y= ',v2.y)

# so we see that x and y are defined inside the class instances v1 and v2

breakpoint()

# now let's move to the next step.
# We saw before the previous breakpoint that we could create variables inside a class
# Wouldn't it be nice to create those variables automatically?
# Let us modify the definition of the class Vector. This definition overrides the previous definition

class Vector():
    def __init__(self,a,b):
#       print('calling __init__')        
        self.x = a
        self.y = b

# we have added a method named __init__ to the class definition. Any method starting and ending with double underscores '__'
# is a special method in Python. They are also called 'magic methods'.
# The special property of the __init__ method is that it is, for now,
# the first method to be called (automatically) after the class is instantiated. The method __init__, in our case, takes 3 arguments
# 'self' is the instance of an object. 'a' and 'b' are user supplied arguments.
# We saw earlier that an empty class definition, consisting of only the keyword 'pass', was enough to instantiate
# the class, allocate memory for it and create an object. You can think of 'self' as this empty object,
# For methods residing inside a class, the 'self' object gets passed automatically. You don't need to worry about it.
# We can see this below:

v1 = Vector(7,8)
v2 = Vector(9,10)

# you can uncomment the print statement inside __init__ to see it being called

# instead of calling Vector() without any arguments, as we did before, we have called it with two arguments.
# the arguments (7,8) and (9,10) are passed to the __init__ method. They become become the second and third arguments of __init__
# the first argument being self, the object itself.
# Let us check that what's inside the object is what we put in.

print('v1.x= ',v1.x, 'v1.y= ',v1.y)
print('v2.x= ',v2.x, 'v2.y= ',v2.y)

breakpoint()


# Now let us add a method 'addvector' inside the class Vector which enables it to add a vector to itself and returns the result

class Vector():
    def __init__(self,a,b):
        self.x = a
        self.y = b

    def addvector(self,v):
#   the method is adding a vector v to itself and returning the resulting vector
#   notice the return statement - it is creating a vector using Vector(xx,yy) and returning that newly created vector
#   in some sense, this definition is recursive. This definition of the method addvector is returning an object of the
#   same class in which it resides.
        xx = self.x + v.x
        yy = self.y + v.y
        return Vector(xx,yy)
        
# Let's test it out. First create two vectors
v1 = Vector(7,8)
v2 = Vector(9,10)

# here we're calling the addvector method which resides in v1. Notice we called it with only one argument: v2.
# but we defined it using two arguments: (self,v). The first argument 'self' is automatically passed. 
v3 = v1.addvector(v2)

# you can see v3.x = 16 and v3.y = 18
print('v3.x= ',v3.x, 'v3.y= ',v3.y)

breakpoint()

# can we add 3 vectors using this approach?
# v4 = v1 + v2 + v3
v1 = Vector(7,8)
v2 = Vector(9,10)  
v3 = Vector(11,12)

# the following statement to add vectors is very awkward, almost unreadable.
# we're adding to v3 the result of adding v1 and v2
v4 = v3.addvector(v1.addvector(v2))
print('v4.x= ',v4.x, 'v4.y= ',v4.y)

# or we can do, which still is more code than necessary
vtemp = v1.addvector(v2)
v4    = v3.addvector(vtemp)

print('v4.x= ',v4.x, 'v4.y= ',v4.y)


breakpoint()

# let's do better. We want to be able to write v4 = v1 + v2 + v3 + ..v_n
# the way to do it is to add a 'magic method' called __add__
# redefine the Vector class

class Vector():
    def __init__(self,a,b):
        self.x = a
        self.y = b

    def __add__(self,v):
        xx = self.x + v.x
        yy = self.y + v.y
        return Vector(xx,yy)
    
# so we're pretty much doing what we did inside the addvector method.
# but because we're defining it inside the 'magic method' __add__, it is linked with the '+' operator
# and therefore, when Python sees v1+v2 it interprets it as v1.__add__(v2)
# the argument 'self' to __add__ is passed automatically


v1 = Vector(7,8)
v2 = Vector(9,10)  
v3 = Vector(11,12)

# so now we are in a position to write

v4 = v1 + v2 + v3

# The Python interpreter performs v1+v2, stores the result in a temporary vector, and then adds v3 to that temporary vector

print('v4.x= ',v4.x, 'v4.y= ',v4.y)

# a complete list of magic methods for Python is here: https://www.python-course.eu/python3_magic_methods.php
