lst = ["a",1,{"x":2}]
print(lst)

x = ({"a":1,"b":2,"c":3})
l = list(x)
print(l)  # [a,b,c]
l_vlaues = list(x.values())
print(l_vlaues)  # [1,2,3]
l_key_val_pair = list(x.items())
print(l_key_val_pair)  # [(a:1),(b:2),(c,3)]

l = [10,20,30]
print(l[0] , l[-1])

x = [1,2]
y = [3,4]
z = (3,4)
x.extend(y)
print(x)
x.extend(z)
print(x)

l = [1,2,3,4]
l.insert(2,"ahamed im here look here at 2 idx")
print(l)
l[2] = 3
print(l)

