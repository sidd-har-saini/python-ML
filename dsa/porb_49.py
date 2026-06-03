"""
group anagrams 
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""



strs = ["eat","tea","tan","ate","nat","bat"]
x = []
def func():
    if not strs:
        return x
    l = []
    op = []
    for i in strs:
        if sorted(i) == sorted(strs[0]):
            l.append(i)
        else:
            continue
    for i in l:
        if i in strs:
            strs.remove(i)
        else:
            continue
   # func()
   # print(strs)

    
    func()
    x.append(l)
    print(x)
func()

    #print(strs)
       



