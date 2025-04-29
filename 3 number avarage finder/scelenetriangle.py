import math

a = float(input("enter first side:"))
b = float(input("enter second side:"))
c = float(input("enter third side:"))

if (a+b>c) and (b+c>a) and (c+a>b):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area will be",round(area ,2))
    
else:
    print("enter vallues that make a triangle")