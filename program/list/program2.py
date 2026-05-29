l = [1,2,3,4,5]

#remove() - remove the specific element from the list which given in parameter 
l.remove(3)
print(l)
#pop() - remove element from the last index
l.pop()
print(l)
#del method deleted elemt from specific index from the list 
del l[2]
print(l)
#clear() remove all element from the list 
l.clear()
print(l)
"""
#output 
[1, 2, 4, 5]
[1, 2, 4]
[1, 2]
[]
"""