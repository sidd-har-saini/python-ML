"""x = "hello"
a = lambda x: x.upper()
#   keyword argument : operation 
print(a(x))
x = int(input("enter the no"))
sq = lambda x : x**2
print(sq(x))"""

x = 4
y = 5
modu = lambda x , y : (x-((x//y)*y))
print(modu(x,y))

x = -1
che = lambda x : "pos" if x>0 else "neg" 
print(che(x))

#x = int(input("e:"))
#check = lambda x : "pos even" if x>0 and x%2==0 else "neg"
#print(check(x))

x = [1,2,3,4,5,6,7,8,9]
res = list(filter(lambda x: x%2==0 , x))
print(res)

def even(x):
    return x%2==0 

lst = [1,2,3,4,5,6,7,8,9]
y = list(filter(even , lst))
print(list(y))

def check(x):
    return x%3 == 0

def check_ge(x):
    return x>5

lst = [1,2,3,4,5,6,7,8,9]
y = list(filter(check_ge,lst))
print(y)

