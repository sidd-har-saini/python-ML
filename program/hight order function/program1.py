"""
high order func is func which we can either pass as argument in function or return function as result 
hof function play important role in fuinctional programming, it increase code modularity , reusablity , and 
readbility 
"""

def HOF(func):
    return func(x)
def func(n):
    return n**n

x = int(input("enter"))
print(HOF(func))

def no(func, x):
    return func(x)
def sqr(x):
    return x**2

x = int(input("enter"))
print(no(sqr,x))

