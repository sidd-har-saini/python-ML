"""
assign funtion to variable 
"""
def func(x):
    return x**2 

f = func
print(f(4))

def greet(name):
    return f"hello {name}"

f = greet
print(f('sidd'))

def cube(x):
    return x**3

def sq(x):
    return x**2

def modu(x,y):
    return (x-((x//y)*y))

a = cube
b = sq
c = modu
print(a(4))
print(b(5))
print(c(99,2))
