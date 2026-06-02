def func(ms):
    def in_func():
        return f"hello {ms}"
    return in_func()

f = func("yeh")
print(f)

def func1(no):
    def sq():
        return no**2
    return sq()
    def cub():
        return no**3
    return cub()
f = func1(3)
f1 = func1(3)

print(f)
print(f)