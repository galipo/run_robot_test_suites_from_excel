"""# global
name='Çinar'

def changeName(new_name):
    # local
     name = new_name
     
     print(name)

changeName( 'Ada')
print(name)"""
#deney-1
"""x=50
def func(x):
    print(f'x is {x}')
    x=100
    print(f'x is changed to {x}')

func(x)
print(x)"""
#deney-2
"""x=50
def func(x):
    global x
    print(f'x is {x}')
    x=100
    print(f'x is changed to {x}')

func(x)
print(x)"""