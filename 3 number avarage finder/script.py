import math
print("3 number avarage finder")
x = int(input("enter first number:"))
y = int(input("enter secound number:"))
z = int(input("enter third number:"))
ans = (x+y+z) /3
print(f"the avarage will be: {ans: 0.2f}")

print ("area of circle")
r = float(input("enter the radius of circle"))
area = math.pi * r**2
print(f"the area of circle , {area:0.2f}")

print ("circumference")
r = float(input("enter the radius of circle"))
area = math.pi * r * 2
print(f"the cricumference {area:0.2f}")

print ("area of triangle")
b = int(input("enter the base of triangle"))
h = int(input("enter the height of triangle"))
area = 0.5 * b * h
print(f"the area will be {area:0.2f}")

print ("area of cylinder")
r = float(input("enter the radius of cylinder"))
h = int(input("enter the height of cylinder"))
area = h * ( 3.14 * r**2 )
print(f"the area will be {area:0.2f}")

print ("area of trapezium")
pl1 = str(input("enter the ist pararell side of the trapezium"))
pl2 = int(input("enter the 2nd pararell side of the trapezium"))
h = int(input("enter the height the trapezium"))
area = 0.5 * (pl1 + pl2) * h
print(f"the area will be {area:0.2f}")

