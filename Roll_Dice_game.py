import random

def  user():
    roll_user = input("Your turn: press any key to roll dice: ")
    if roll_user:
        dice_user = random.randint(1,6)
        print("You rolled: ", dice_user)
        return dice_user
def computer():
    dice_computer = random.randint(1, 6)
    print("Computer rolled: ", dice_computer)
    return dice_computer
def game():
    print("Welcome to the game")

def rule():
    print("Rules","1. No. of Turns: Your Choise" , "2. You roll a dice and the computer rolls a dice.", "3. The one with the higher score wins.", "4. Player Score equal Computer Score match Tie" , "Good luck!", sep = "\n")
    print("Let's start the game")
    print("--------------------------------------------------")
    No_of_Turns = int(input("Enter the number of turns you want to play:"))
    print("--------------------------------------------------")
    return No_of_Turns
def game():
    turns = rule()
    user_score = 0
    computer_score = 0
    while turns > 0:
        user_roll = user()
        computer_roll = computer()
        user_score = user_score + user_roll
        computer_score = computer_score + computer_roll
        turns -= 1
    if user_score > computer_score:
        print("--------------------------------------------------")
        print(f"Your Score: {user_score}")
        print(f"Computer's Score: {computer_score}")
        print(f"You win!")
    elif user_score < computer_score:
        print("--------------------------------------------------")
        print(f"Your Score: {user_score}")
        print(f"Computer's Score: {computer_score}")
        print(f"Computer win!")
    else:
        print("--------------------------------------------------")
        print("It's a tie!")
        
game()
