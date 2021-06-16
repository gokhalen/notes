# These functions __radd__ are only called if the left operand does not support the corresponding operation using __add__ and returns NotImplemented and the operands are of different types. 

class Foo():
    def __init__(self,n):
        self.n = n

    def __add__(self,r):
        return NotImplemented

    def __str__(self):
        return f'Foo({self.n})'


class Bar():
    def __init__(self,n):
        self.n = n

    def __radd__(self,left):
        print('Falling back on __radd__')
        return Foo(self.n+left.n)

print(Foo(5)+Bar(6))
