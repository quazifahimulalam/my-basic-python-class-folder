try:
    age = int(input("enter your age:"))
    
    if age%2 == 0:
        print("age is even")
    else:
        print("age is odd.")
        
except ValueError as e:
    print("error:" , e)