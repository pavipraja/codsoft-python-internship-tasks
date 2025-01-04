import random

options = ("rock","paper","scissors")
running = True

while running:
    player = None
    Computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock/paper/scissors):").lower()

    print(f"Player :{player}")
    print(f"Computer :{Computer}")

    if player == Computer :
        print("It's a tie")
    elif player == "rock" and Computer == "scissors":
        print("You win!")
    elif player == "paper" and Computer == "rock":
        print("You win!")
    elif player == "scissors" and Computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    choice = input("Play again(y/n):").lower()
    if not choice == "y":
        running = False
print("Thanks for playing")