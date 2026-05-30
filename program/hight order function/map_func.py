"""
map() function in python is hight order function in , we pass funcction as argumnet to which applied to each 
element in the iterable list 
"""
x = [1,2,3,4,5,6]
res = list(map(lambda x: x**2 , x))
print(res)

a = [1,2,3,4,5,6,7,8]
b = [2,3,4,5,5,6,6,3]
x = []
res = list(map(lambda x,y: x-((x//y)*y) , a,b))
print(res)

a = ["hello" , "python","hey"]
res = list(map(lambda x: x.upper() , a))
print(res)
res = list(map(lambda x: len(x) , a))
print(res)

x = ['1','2','3']
res = list(map(lambda x: int(x) , x))
print(res)
print(x)
x = ['a','b','c']
res = list(map(lambda x: ord(x),x))
print(res)

x = ['apple','banana','cherry']
l =[]
for i in x:
    l.append((i,len(i)))
print(l)
l = ['apple','banana','cherry']
res = list(map(lambda i: ((i,len(i))),l))
print(res)

l = [[1,2],[3,4],[4,5]]
x = []
for i in range(len(l)):
    y = l[i][0] + l[i][1]
    x.append(y)
print(x)
x = [[1,2],[3,4],[5,4]]
y = list(map(lambda x : x[0] +x[1] , x))
print(y)