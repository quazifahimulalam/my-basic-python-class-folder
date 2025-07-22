print("program celcius to farenhight.")

print("chose your convertion:")

print("1. celcius to farenhight")
print("2. farenhight to celcius")
print("3. exit.")

choice = int(input("enter your choice:"))

if choice == 1:
    cel = float(input("enter the celcius value:"))
    far = (cel * 9/5) + 32
    print(f"celcius to farenhight will be:{far}")
elif choice == 2:
    far = float(input("enter the farenhight value:"))
    cel = (far - 32) * 5/9
    print(f"farenhight to celcius will be:{cel}")
elif choice == 3:
    print("exiting program goodbye.")
    
