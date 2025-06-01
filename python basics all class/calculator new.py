def operations():
    print("seclect an operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

def take_input():
    choice = int(input("enter the choice 1/2/3/4 :"))
    if choice in (1,2,3,4):
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))
        return choice ,num1 , num2
    else:
        print("Invalid input.Please retry.")
        return take_input()
    
def calculate():
    choice , a , b = take_input()
    if choice == 1:
        result = a+b
        print(f"the result of {a} + {b} is: {result:0.2f}")
    elif choice == 2:
        result = a-b
        print(f"the result of {a} - {b} is: {result:0.2f}")
    elif choice == 3:
        result = a*b
        print(f"the result of {a} * {b} is: {result:0.2f}")
    else:
        result = a/b
        print(f"the result of {a} / {b} is: {result:0.2f}")
        
if __name__ == "__main__":
    print("---------Calculator---------")
    operations()
    print("----------------------------")
    calculate()
    print("----------------------------")