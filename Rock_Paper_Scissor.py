import random
def game():
    flag= 1
    
    while flag:
        user = input("Enter a choice (rock, paper, scissors) ").lower()
        options = ["rock", "paper", "scissors"]
        if user not in options:
            print("Invalid input")
            game()
        computer = random.choice(options)
        print(f"Computer chose {computer}")
        if user == computer:
            print("It's a tie")
        elif user == "rock" and computer == "scissors":
            print("You win")
        elif user == "paper" and computer == "rock":
            print("You win")
        elif user == "scissors" and computer == "paper":
            print("You win")
        else:
            print("You lose")
        print('Exit press 0: continue press 1:')
        flag = int(input())

print("Welcome to Rock, Paper, Scissors!")

game()
