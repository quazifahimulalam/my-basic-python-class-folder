ft = int(input("enter your height in feet:"))
inch = int(input("enter your height in inch:"))

meter = (ft * 12 + inch)* 0.0254

kg = int(input("enter your weight in kg:"))

bmi = kg/meter**2

print("your bmi is,",bmi)

if bmi < 18.5:
    print("your are underweight.")
elif 18.5 <= bmi <= 24.9:
    print("you are perfectly weighted.")
elif 25 <= bmi <=29.9:
    print("you are overweight.lose some weight")
elif 30 <= bmi <= 34.9 :
    print("hey fatty lose some weight if you want to live another year")
else:
    print("bro your beyond cooked.BMI",bmi,"IS CRAZY")