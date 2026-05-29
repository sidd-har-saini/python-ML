"""
txt = "hello world"
print(txt.capitalize())
capitalize()--- convert first character of string into capital

t = " hello world"
print(t.capitalize())

center() - it center align the charcter/string with in the give space , it space padded on both side of string
txt = "hello"
s = txt.center(10,"#")
print(s)
s = txt.center(20,"-")
print(s)


count() - this method return the count of substring appeare in the string
txt = "hello world"
print(txt.count("o"))
print(txt.count("h"))

encode() - it convert character into byte , it's by deafult encoding format is utf-8 
string.encode(encoding="ascii",error="ignore")

txt = "hello ö(invlaid)"
print(txt.encode(encoding="utf-8",errors="replace"))
print(txt.encode(encoding="ascii",errors="ignore"))



txt = "hello greek people"
r1 = txt.endswith("greek")
r2 = txt.endswith(("greek","people","hello"))
r3 = txt.endswith("o",1,5)
print(r1)
print(r2)
print(r3)

"""