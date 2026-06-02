"""x = "hello\tworld\tspace"
y = x.expandtabs()
print(y)

x = "hello world"
print(x.find("world"))
print(x.find("o"))

x = "hello"
y = "world"
print("this line %s %s"  % (x,y))

name ="siddharth"
age = 19
print("name is %s age %s" %(name , age))

name = "siddharth"
print("{}".format(name)) 
print("{} motherfucker cunt".format(name))

x = "name"
y = f"{x} !"
print(y)"""

from  string import Template
n = "hello"
s = Template("$n1 world")
print(s.substitute(n1=n))

name = "hello"
print(f"{name} world")
print("{} world".format(name))
print(name , "world")
