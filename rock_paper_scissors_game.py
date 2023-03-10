import random

while True:
    print("Welcome to the Rock Paper Scissors Game!")
    print("Rules: Rock breaks scissors, paper covers rock and scissors cuts paper\nCan you beat the Computer?\n")
    player = input("Choose (Rock, Paper or Scissors): ")
    game_list = ["rock", "paper", "scissors"]
    computer = random.choice(game_list)
    print(f"\nYou chose {player}, Computer chose {computer}.\n")

    if player == computer:
        print(f"You both chose {player}. Its a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock breaks Scissors You win!")
        else:
            print("Paper covers Rock Computer wins!")
    elif player == "paper":
        if computer == "scissors":
            print("Scissors cuts Paper Computer wins!")
        else:
            print("Paper covers Rock You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Rock breaks Scissors Computer wins!")
        else:
            print("Scissors cuts Paper You win!")

    new_game = input("Thanks for playing!\nDo you want to play again? (Y/N): ")
    if new_game.lower() != "y":
        break

