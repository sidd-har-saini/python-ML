def deco(f):
    def wrapper():
        print("bef dec func")
        f()
        print("aft dec func")
    return wrapper
@deco
def func():
    print("greeting")
func()

def deco(f):
    def wrapper():
        print("bef deco")
        f()
        print("aft deco")
    return wrapper
@deco 
def func():
    print("hello world")
func()

def deco(f):
    def wrapper():
        print("start")
        f()
        print("entd")
    return wrapper

@deco
def func():
    print("hello")
func()

def rep_deco(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper

@rep_deco
def hi():
    print("hello")
hi()

def add_deco(f):
    def wrapper(*args,**kwargs):
        res = f(*args,**kwargs)
        print(res)
        return res
    return wrapper

@add_deco
def func(a,b):
    return a+b
print(func(3,4))

def func(a,b):
    return a+b

f = func
print(f(1,2))
print(func(1,2))