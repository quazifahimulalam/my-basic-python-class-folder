a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if a>b and a>c:
    print("first number is the biggest")
elif b>a and b>c:
    print("second number is the biggest")
else:
    print("the third number is the biggest")