n = int(input("enter a number:"))

s = 0
temp = n
while temp > 0:
    digit = temp%10
    s = s + digit ** 3
    temp = temp // 10
if n == s :
    print(n, "is a armstrong number.")
else:
    print(n ,"is not an armstrong number")
    