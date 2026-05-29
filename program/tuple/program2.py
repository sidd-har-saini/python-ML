tup = (1,2,3,4,5,6)
print(tup[1])
print(tup[1:4])
print(tup[-1:2])
print(tup[-1:-3:-1])
print(tup[::-1])

tup = ('greek','for','greek')
a,b,c = tup
print(a)
print(b)
print(c)


t = (1,2,3)
t2 = (3,4,5)
t3 = t2+t
print(t3)

t = tuple('hello')
t2 = (1,2,3)
e = t+t2
print(e)

f =([1,2],'hello')
g = (1,2,3)
tup = f+g
print(tup)

tup = tuple("helloworldhey")
print(len(tup))
print(tup[3:])
print(tup[3:len(tup)])
print(tup[1:len(tup):3])

try :
    tup = (1,2,3,4,5)
    del tup 
    print(tup)
except Exception as e:
    print(e)

tup = (1,2)
a,*b,c = tup
print(a)
print(b)
print(c)