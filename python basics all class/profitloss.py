b = float(input("enter the buying price:"))
s = float(input("enter the selling price:"))
if b>s :
    print("you have made a loss of", b-s)
elif s>b :
    print("you have made a profit of" , s-b)
else:
    print("you made nither a profit of a loss")