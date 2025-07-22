upper = int(input("enter the upper number"))
lower = int(input("enter the lower number"))

for i in range(lower,upper + 1 ):
    if i > 1 :
        for n in range(2,i):
            if i%n == 0:
                break
        else:
            print(i)
            


weight = int(input("enter your weight in kilograms:"))
height = float(input("enter your height in meter:"))

bmi = weight / (height**2)

if bmi > 25.0:
    print("You are obese class 3.Your bmi is:",bmi)
elif bmi <= 24.9 and bmi >= 18.5:
    print("You are healthy.Your bmi is:",bmi)
elif bmi <= 18.4 and bmi >= 17.0:
    print("You are underweight.Your bmi is:",bmi)
else:
    print("you are very underweight")