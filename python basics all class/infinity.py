while True :
    n = input("enter a number or type exit to leave :")
    if n.lower == "exit" :
        print("exiting program:")
        break
    else:
        n = int(n)
        if n%2 == 0:
            print("The number is even")
        else:
            print("The number is odd")