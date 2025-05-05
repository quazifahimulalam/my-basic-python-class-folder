year = int(input("enter a year:"))

if year % 400 == 0 :
    print("the year is a leap year")
elif year %100 == 0:
    print("the year is not a leap year")
elif year %4 == 0:
    print("it is a leap year")
else:
    print("it is a leap year")