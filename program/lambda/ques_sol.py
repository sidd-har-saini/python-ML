ls = [1,2,3,4,5,6,7,8,9]
res = list(map(lambda x : x**2, ls))
print(res)
res2 = [val** 2 for val in ls]
print(res2)
res3 = [val**2 for val in range(1,10)]
print(res3)

#---------------------------------------------------------------
ls = [1,2,3,4,5]
res = list(map(lambda x: x*2 , ls))
print(res)
res1 = [val*2 for val in ls]
print(res1)
#---------------------------------------------------------------------
words = ["python","java","c"]
res = list(map(lambda x: len(x), words))
print(res)
res1 = [len(val) for val in words]
print(res1)
#----------------------------------------------------------------------
nums = [1,2,3,4,5,6,7,8]
res = [val for val in nums if val%2==0]
print(res)
res1 = list(filter(lambda x : x%2==0 , nums))
print(res1)
#-----------------------------------------------------------------------
res = [val for val in range(1,20) if val%3==0]
print(res)
x = [val for val in range(1,20)]
res2 = list(filter(lambda num:num%3==0 , x))
print(res2)
#------------------------------------------------------------------------
names = ["Ram","Shyam","Anshu","AI"]
res1 = [val for val in names if len(val)>3]
res = list(filter(lambda s: len(s)> 3,names))
print(res1)
print(res)
#--------------------------------------------------------------------------
nums = [1,2,3,4,5]
res = ["odd" if val %2==0 else "even" for val in nums]
print(res)
res2 = list(map(lambda x : "odd" if x%2==0 else "even" , nums))
print(res2)
#---------------------------------------------------------------------------
nums = [-2,-1,0,1,2]
res = ["positive" if num>0 else "negative" for num in nums] 
print(res)
res1 = list(map(lambda nums: "positive" if nums>0 else "negative" , nums))
print(res1)
#---------------------------------------------------------------------------
mat = [[1,2],[3,4],[5,6]]
res = [val for row in mat for val in row]
print(res)
res = list(filter(lambda x : x, mat))
print(res)
#---------------------------------------------------------------------------
#[(1,1),(1,2),(2,1),(2,2)]
res = [(x,val) for x in range(1,3) for val in range(1,3)]
print(res)