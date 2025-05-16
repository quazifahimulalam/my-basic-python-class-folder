unit = int(input("enter your units:"))

if unit <= 100:
    bill = unit * 1.5
    print("your bill is :",bill)
elif unit <= 200:
    bill = (100 * 1.5) + (unit - 100) * 2.5
    print("your bill is :",bill)
elif unit <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + (unit - 200) * 4
    print("your bill is:" , bill)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (unit - 300) * 6
    print("your bill is" , bill)
