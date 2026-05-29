a = [("a", 1), ("b", 2), ("c", 3)]
x = dict(a)
print(x)

res = {}
for key,val in a:
    res[key] = val
print(res)