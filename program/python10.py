x = {"name":"john","l_name":"wick"}
print("{name} {l_name} excumnicado".format_map(x))

x = {"name" :"siddharth",
"age":19}
s = "{name} {age} stat active".format_map(x)
print(s)

dict = {
    "name": ["john wick","shinchan"],
    "need": ["gun","girl"],
    "toy":["quantum rob","gun"]
}
x = "{name[0]} require {need[0]} and an another {toy[1]}".format_map(dict)
print(x)

y ="123"
x ='12a'
print(x.isalnum())
print(x.isalpha())
print(x.isnumeric())
print(y.isnumeric())

x = ("hello","world","and","hey","there")
t = " +".join(x)
print(t)

x = "hello"
fil = "*"
leng = 3
print(x.ljust(leng,fil))

x = "hello world"
y = x.partition(" ")
print(y)

x = "hello a"
y=x.replace("a","python")
print(y)

x = 'name is'
y = x.replace("name","is")
print(y)

x = "hello\n\nworld\nhello"
print(x.splitlines())
print(x.splitlines(keepends=True))

x = "hello\n\n\nworld\n\nhello\n"
print(x.splitlines())
print(x.splitlines(keepends=True))

x = "-72"
p = x.zfill(2)
print(p)