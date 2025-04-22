def generateRandom(user_input):
    hashValue = hash(user_input)
    randomChoice = hashValue % 3
    return randomChoice

def winner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "It's a tie!"
    elif ((playerChoice == 0 and computerChoice == 2) or (playerChoice == 1 and computerChoice == 0) or (playerChoice == 2 and computerChoice == 1)):
        return "You win!"
    else:
        return "You lose!"

def choice(choice):
    choices = ["Rock", "Paper", "Scissors"]
    return choices[choice]

def playgame():
    print("Welcome to Rock, Paper, Scissors!")

    playerChoice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    if playerChoice == "rock":
        playerChoice = 0
    elif playerChoice == "paper":
        playerChoice = 1
    elif playerChoice == "scissors":
        playerChoice = 2
    else:
        print("Invalid choice! Exiting game.")
        return

    user = input("Enter a string or number to generate randomness for the computer's choice: ")
    computer = generateRandom(user)

    print(f"You chose: {choice(playerChoice)}")
    print(f"Computer chose: {choice(computer)}")

    result = winner(playerChoice, computer)
    print(result)
    again=input("do you want to play again?\n(yes/no)\n").lower()
    if again == "yes":
        playgame()
    else:
        print("Thanks for playing!")
        return
playgame()