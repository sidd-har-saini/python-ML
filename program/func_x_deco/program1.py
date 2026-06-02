def fun():
    print("ehloo")
fun()
def fun():
    return "hello"
print(fun())
def fun(x):
    return x**4
print(fun(3))


def fun(*args ,**kwargs):
    print("*args positional argument")
    for i in args:
        print(i)
    print("**kwargs keyword argument as dick")
    for key,val in kwargs.items():
        print(f"{key}:{val}")
    
fun("hello","hell","yo!!!", name = "siddharth" , l_name = "saini")


def sum_all(*args):
    l = []
    for i in args:
        l.append(i)
        x = sum(l)
    print(x)
sum_all(1, 2, 3, 4)
from functools import reduce
def add(*args):
    y = reduce(lambda x,y : x+y , args)
    print(y)
add(1,2,3,4)

def greater(*args):
    print(args)
    largest = args[0]
    for i in range(0,len(args)-1):
        if args[i] > largest:
            largest = args[i]
    print(largest)

    #print(i)
greater(10, 5, 20, 8)
# 20
#def greater(*args):

def cunts(*args):
    count = 0
    for i in args:
        count = count+1
    
    print(count)
cunts("a","b","c","d")

def cunts(**kwargs):
    for key,values in kwargs.items():
        print(key , values)
    print(kwargs.values())
    val = 'Anshu'
    if val in kwargs.values():
        print(val)
        print("found")
    else:
        print("not found")
    
cunts(name="Anshu", age=20)

def deco(f):
    def wrapper(*args,**kwargs):
        print("before")
        res = f()
        print("after")
        return res
    return wrapper

@deco 
def func():
    print("hello")
func()


def deco(f):
    def wrapper(*args,**kwargs):
        res = f(*args,**kwargs)
        return res
    return wrapper

class stud:
    @deco
    def func(self,x,y):
        print(x+y)

obj = stud()
obj.func(5,8)