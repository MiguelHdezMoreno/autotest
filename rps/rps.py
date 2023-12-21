from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
computer_choice = options[randint(0, 2)]

def user_choice():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    if user_choice.upper() == "ROCK":
        return "ROCK"
    elif user_choice.upper() == "PAPER":
        return "PAPER"
    elif user_choice.upper() == "SCISSORS":
        return "SCISSORS"
    else:
        print("Please enter a valid choice")
        user_choice()

def play_RPS():
    user = user_choice()
    print("Your choice: " + user)
    print("Computer choice: " + computer_choice)
    if user == computer_choice:
        print("It's a tie!")
    elif user == "ROCK" and computer_choice == "PAPER":
        print("You lose!")
    elif user == "ROCK" and computer_choice == "SCISSORS":
        print("You win!")
    elif user == "PAPER" and computer_choice == "ROCK":
        print("You win!")
    elif user == "PAPER" and computer_choice == "SCISSORS":
        print("You lose!")
    elif user == "SCISSORS" and computer_choice == "ROCK":
        print("You lose!")
    elif user == "SCISSORS" and computer_choice == "PAPER":
        print("You win!")

play_RPS()