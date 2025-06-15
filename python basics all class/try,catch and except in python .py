try:
    print("bill calculator.")

    owe_amount = int(input("please enter your bill amount:"))
    paid_amount = int(input("please enter how much you paid:"))
    pay = 0
    if owe_amount > paid_amount:
        pay = owe_amount - paid_amount
        print(f"your payment was not sufficient enough.you need to pay {pay} tk more")
    elif owe_amount < paid_amount:
        pay = paid_amount - owe_amount
        print(f"your payment was too much.You need to pay {pay} tk more")
    else :
        print(f"your payment was sufficient")
        
except ValueError as e:
     print("error:" , e)