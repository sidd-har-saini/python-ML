"""
txt = "hello"
try :
    del txt 
    print(txt)

except Exception as e:
    print(e)

"""

#---------------------------------------------------------------------------------------------------------
"""#----------------------------------------------------------------------------------------------------------
tx = "hello"
tx2 = "hey"
try :
    s = "yo" + tx[:-1]
    s2 = tx.replace("hello","yo")
    print(s)
    print(s2)

except Exception as e:
    print(e)  
"""

"""
txt = "hello "
print(len(txt))

s = "            hello "
print(s.strip())

s = "python is fun"
s.replace("fun","awsome")
print(s)
print(s.replace("fun" ,"awsome"))

"""
#----------------------------------------------------------------------------------------------------------
"""
s = "hello"
s2 = "world"
print(s+s2)
print(3*s)
"""
#----------------------------------------------------------------------------------------------------------
"""
a = "siddharth"
b = "saini"
print(f"{a} {b}")
print(f"name is : {a} and l_name is {b}")
"""
#----------------------------------------------------------------------------------------------------------
name = input("enter name")
age = int(input("enter age"))
txt = "this text contain name:{} and age:{}".format(name, age)
print(txt)

#----------------------------------------------------------------------------------------------------------
s = "greek"
print("G"in s)