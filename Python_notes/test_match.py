# https://benhoyt.com/writings/python-pattern-matching/

class Car:
    __match_args__ = ('key','name')

    def __init__(self,key,name):
        self.key  = key
        self.name = name


# expr = eval(input('Expr: '))

exprlist = [(0,12),
            ('a',12.2,'c'),
            {'foo':123},
            [1,2,11.4,112.7],
            {'x':77,'y':88,'z':99},
            Car(key='12',name='Tesla'),
            Car(key='123',name='Mercedes'),
            1,
            'one',
            'I',
            ['a','x','y'],
            ['b','x','y'],
            ['d','x','y'],
            ['x','x','z','zz','zzz'],
            ['x','y','z','zz','zzz']        
           ]

for expr in exprlist:
    match expr:

        case (0,x):
            print(f'(0,{x})')

        case ('a',x,'c'):
            print(f"'a',{x},'c'")

        case {'foo':bar}:
            print(f"{{'foo':{bar}}}")

        case [1,2,*rest]:
            print(f'[1,2,*{rest}]')

        case {'x':x,**kw}:
            print(f"{{ 'x':{x}, **{kw} }}")

        case Car(key=xx,name='Tesla'):
            print(f'Car({xx},"TESLA")')

        # if this general case is before the previous case
        # the previous case will never fire
        case Car(xx,yy):
            print(f'Car({xx},{yy})')
            
        case 1 | 'one' | 'I':
            print('one')

        case ['a' | 'b' as ab, *c]:
            print(f'{ab}, {c}')

        case (x,y,*c) if x == y:
            print(f'{x},{y},*{c}')
             
        case _:
            print('no match')
