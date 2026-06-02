"""
x = int(input("enter"))
y = int(input("enter"))
z = int(input("enter"))
res = (lambda x,y,z : sorted((x,y,z))[1]) 
print(res(x,y,z))
"""

x = [1,2,3,4,5]
y = [val**val for val in x ]
print(y)
x = [2,3,4,22,44,11,55,223,656,32,654,535,6543,99934332]
y = [val for val in x if val%2==0]
print(y)
x = [1,2,3,4]
y = [(row , col) for row in range(len(x)) for col in range(len(x))]
print(y)
res = [val for row in y for val in row]
print(res)


#returning multiple result 

cal = lambda x,y : (x+y , x-y)
print(cal(2,3))
cal = lambda x,y : ((x//y) ,(x-((x//y)*y)))
print(cal(25,3))
from functools import reduce
x = [2,4,5,7,5,7,2,6,3]
y = reduce(lambda x,y : x*y , x)
print(y)
y_ = reduce(lambda x,y : x//y , x)
print(y_)

x =[5,1,8,3,9,2]
y = reduce(lambda a, b: a if a>b else b , x)
print(y)
y_ = reduce(lambda a,b : b if a>b else a,x)
print(y_)
x = ["I","Love","Python"]
y = []
for i in x:
    y.append(i)
print(" ".join(y))
y = reduce(lambda a,b : a+" "+b , x)
print(y)

#--------------------------------------------------------
x = ["cat","elephant","dog","python"]
y = reduce(lambda x,y : x if len(x)>len(y) else y , x)
print(y)

#----------------------------------------------------------
x = [1,2,3,4,5,6]
y = reduce(lambda acc, curr : acc+curr if (curr%2==0) else acc , x)
print(y) 
