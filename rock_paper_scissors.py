import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Enter Choice: \n").lower()
if user_choice in choices:
    computer_choice = random.choice(choices)
    print("Computer Chose:", computer_choice)
    if(computer_choice == "rock" and user_choice == "paper"):
        print("User Won!")
    elif(computer_choice == "paper" and user_choice == "rock"):
        print("Computer Won!")
    elif(computer_choice == "paper" and user_choice == "scissor"):
        print("User Won!")
    elif(computer_choice == "scissors" and user_choice == "paper"):
        print("Computer Won!")
    elif(computer_choice == "rock" and user_choice == "scissors"):
        print("Computer Won!")
    elif(user_choice == computer_choice):
        print("Draw Game!")
    else:
        print("User Won!")
else:
    print("Invalid Choice")
