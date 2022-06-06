import random

while True:
    userAction = input("Enter a choice (rock, paper, scissors): ")
    possibleActions = ["r", "p", "s"]
    computerAction = random.choice(possibleActions)
    print(f"\nYou chose {userAction}, computer chose {computerAction}.\n")
    
    if userAction == computerAction:
        print(f"Both Players selected{userAction}.It's a tie!")
    
    elif userAction == "r":
        if computerAction == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose. ")
    elif userAction == "p":
        if computerAction == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose. ")
    elif userAction == "s":
        if computerAction == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose. ")
            
    else:
        print("User input is invalid")
            
            
    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        break    

    