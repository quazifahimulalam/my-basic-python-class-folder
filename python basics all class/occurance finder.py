s = input("enter a sentence:").lower()
c = input("the character of which the occurance needs to be found:")

i = 0
count = 0

while i < len(s):
    if s[i] == c:
        count = count + 1
i = i + 1
print(f"total occurance of {c} is : {count}")