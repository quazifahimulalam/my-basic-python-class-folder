import random

def display_rules():
    print("\n--- Game Rules ---")
    print("rock beats scissors")
    print("scissors beat paper")
    print("paper beats rock\n")

def determine_winner(user, computer): 
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def rock_paper_scissor():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_score = 0
        computer_score = 0
        round_number = 1

        print("\nWelcome to the rock-paper-scissors game") 
        print("type 'rules' to see how to play or 'quit' to exit the game.\n")

        while True:
            print(f"--- round {round_number} ---")
            print("available choices: rock, paper, scissors")
            user_choice = input("enter your choice: ").lower()

            if user_choice == "quit":
                print("Thanks for playing")
                print(f"Final score => you: {user_score} | computer: {computer_score}\n") 
                break
            elif user_choice == "rules":
                display_rules()
                continue
            elif user_choice not in choices:
                print("Invalid input. Please enter rock, paper, or scissors.")  
                continue

            computer_choice = random.choice(choices)
            print(f"computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice) 

            if result == "tie":
                print("It's a tie")  
            elif result == "user":
                print("You win this round")  
                user_score += 1
            else:
                print("Computer wins this round")
                computer_score += 1

            print(f"Current scores => you: {user_score} | computer: {computer_score}")
            round_number += 1

        play_again = input("Would you like to play again? ")  
        if play_again.lower() != "yes": 
            print("Goodbye")
            break

if __name__ == "__main__":
    rock_paper_scissor()
