def func(f):
    def wrapper(*args , **kwargs):
        print('method stater')
        res = f(*args , **kwargs)
        return res
    return wrapper

class stud:
    @func
    def fun(self):
        print("hello")

obj = stud()
obj.fun()

def deco(f):
    def wrapper():
        print("<<before")
        f()
        print("<<after")
    return wrapper

@deco
def func():
    print("hello")

func()

def deco(f):
    count = 0 
    
    def wrapper(*args,**kwargs):
        nonlocal count
        count = count+1
        print(f"class {count}")
        f(*args,**kwargs)
    return wrapper

class s:
    @deco
    def func(self):
        print("hello")

obj = s()
obj.func()
obj.func()
obj.func()

def outer():
    x = 10
    def inner():
        nonlocal x
        x=x+1
        print(x)

    inner()
outer()

def deco(f):
    def wrapper(a,b):
        add = f(a,b)
        print('add',add)
        double = add * a
        print('multi' , double)
        return add
        return double
    return wrapper

@deco
def func(a,b):
    return a+b
print(func(3,5))


def deco(f):
    def wrap(*args):
        #print(x,y)
        print("argument:" ,args[1:])
        print("function name:::" , f.__name__)
        res = f(*args )
        return res
    return wrap

class per:
    @deco
    def func(self,x,y):
        return x+y
obj = per()
obj.func(2,4)

