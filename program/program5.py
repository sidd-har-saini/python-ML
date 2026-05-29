a = int(input("enter the no"))
b = int(input("enter the divident"))

gt = max(a,b)

while True:
    if gt % a == 0 and gt %b == 0:
        print(gt)
        break
    else:
        gt = gt+1 
        