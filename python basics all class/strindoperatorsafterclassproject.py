text = str(input("please enter a line:"))

capitalised  = text.capitalize()
title  = text.title()

print("the line capitalised," , capitalised)
print("the line titled," , title)


line = str(input("enter the line:"))
find = str(input("enter the word you want to find:"))
x = line.index(find)
print("the word location is," , x)