"""
x = int(input("enter"))
y = int(input("enter"))
z = int(input("enter"))
res = (lambda x,y,z : sorted((x,y,z))[1]) 
print(res(x,y,z))
"""
x = [("A",90), ("B",75), ("C",85)]
res = list(sorted(lambda y : x[y]  ))
print(res)