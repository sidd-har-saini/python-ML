"""
we can also store funtion in data structur ike dict and list
"""

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def sq_x(x):
    return x**2
def modulo(x,y):
    return (x-((x//y)*y))

d = {
    'addition' : add,
    'subtraction' : sub,
    'multi' : multi,
    'sq_x': sq_x,
    'modulo' : modulo
}
#d_d = [add,sub,multi,sq_x,modulo]
#print(d_d[add](1,2))
print(d['addition'](4,4))
print(d['subtraction'](3,1))
print(d['modulo'](3,4))



#------------------------------------------
#pass function as argument 
def deco(f):
    def wrapper():
        print("hello")
        f()
    return wrapper

@deco
def func():
    print("hello")
func()

def deco(f):
    def wrapper(*args , **kwargs):
        print("before")
        f(*args,**kwargs)
        print("after")
    return wrapper

@deco 
def func(x,y):
    print(x+y)
func(2,4)

def deco(f):
    def wrapper(*args , **kwargs):
        res =f(*args,**kwargs)
        return res
    return wrapper

@deco
def func(x,y):
    return x**y
print(func(3,4))


def deco(f):
    def wrapper(*args, **kwargs):
        f()
        print("deco")
    return wrapper

@deco
def func(x,y):
    return x+y
print(func(4,5))

def deco(f):
    def wrapper():
        print("hello")
        f()
        print("pp")
    return wrapper

@deco
def func():
    print("hello")
print(func())