l = [1,2,3]
l2 = l
l2[2] = 45
print(l)
print(l2)

l = [1,2,3]
l2 = l.copy()
print(l2)
l2[2] = 34
print(l2) 
print(l)

l = [1,2,4]
print(l.index(2))
l.reverse()
print(l)
l.reverse()
print(l)

l = [2,1,3,4,55,63,22,66,8]
l.sort()
print(l)
l.sort(reverse=True)
print(l)