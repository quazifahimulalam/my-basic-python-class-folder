import array

arr = array.array('i' , [24,26,2,72,4,45,46,34,56,43,56,33,56])

print("array contents:" , list(arr))

print("1. insert")
print("2. search")
print("3. delete")
print("4. exit")

choice = input("enter your choice (1-4)")

if choice == '1':
    val = int(input("enter value to insert:"))
    arr.append(val)
    print(f"{val} inserted")
    print("array contents:" , list(arr))

elif choice == '3':
    val = int(input("enter value to delete:"))
    if val in arr:
        arr.remove(val)
        print(f"{val} deleted")
        print("array contents:" , list(arr))
    else:
        print(f"{val} not found in a array")
        
elif choice == '2':
    val = int(input("enter value to search:"))
    if val in arr:
        print(f"{val} found in index{arr.index(val)}.")
    else:
        print(f"{val} not found in array")
        
elif choice == '4':
    print("exiting the program.")


