r = str(input("do you have a medical reason? yes/no:"))
p = int(input("enter your attendence percentage:"))
 
r = r.lower()
 
if r == "yes":
     if p >= 60:
         print("you can take the exam")
     else:
        print("you cannot take the exam")
elif r == "no":
    if p >= 75:
        print("you may take the exam")
    else:
        print("you cannot take the exam")
else :
    print("you cannot take the exam")