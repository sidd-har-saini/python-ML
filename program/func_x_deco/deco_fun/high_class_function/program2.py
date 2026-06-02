"""
passing function as argument 
"""

def greet(name):
    return f"hello {name}"

def func( f , name):
    return f(name)

print(func(greet , "sidd"))


def sq(x):
    return x**2

def cude(x):
    return x**3

def apply(func , val):
    return func(val)

print(apply(sq , 5))
print(apply(cude, 55))

def add_one(x):
    return x+1

def add_two(x,y):
    return x+y

def apply(func , val ):
    return (func(val))

def apply2(func ,val , val2 = 0):
    return (func(val,val2))

print(apply(add_one , 4))
print(apply2(add_two ,5,6))
