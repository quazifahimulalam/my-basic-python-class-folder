import random

print("this is the number guessing game.")
print("guess the number petween 1-10 .")
print("you have five attempts per rnd.")
print("type 'quit' anytime to exit the game.")

score = 0

while True:
    secretnumber = random.randint(1,10)
    attempts = 0
    maxattempts = 5
    
    while attempts < maxattempts:
        userinput = input(f"enter your guess on attempt {attempts + 1 } out of {maxattempts} ")
        if userinput.lower() == "quit" :
            print("you have chosen to quit.")
            print(f"your final score: {score}")
            exit()
        try:
                guess = int(userinput)
        except ValueError:
                print("invalid unput. please enter a number between 1-10")
                continue
        if guess < 1 or guess > 10:
                print("your guess must be between 1 to 10")
                continue
        attempts += 1
        
        if guess < secretnumber:
            print ("too low. guess again")
            score -= 5
            print(f"you have {maxattempts - attempts} attempts left")
            print(f"your current score is {score}")
        elif guess >secretnumber:
            print ("too high. guess again")
            score -= 5
            print(f"you have {maxattempts - attempts} attempts left")
            print(f"your current score is {score}")
        else:
            print ("congratulations.you guessed the correct number.")
            score += 10
            print(f"you have used {attempts} attempts")
            print(f"your current score is {score}")
            break
        
    else:
        print("game over . your are out of attempts")
        print(f"the correct munber was: {secretnumber}")
        print(f"your final score is: {score}")
        break