import random

while True:
    print("Welcome to Rock Paper Scissors! Can you beat the Computer?")
    game_list = ["Rock", "Paper", "Scissors"]
    player = input("Choose (Rock, Paper or Scissors): ")
    computer = random.choice(game_list)
    print(f"\nYou chose {player}, Computer chose {computer}.\n")
    if player == computer:
        print("Its a Tie!")
    elif player == "Rock":
        if computer == "Scissors":
            print("Rock breaks Scissors You win!")
        else:
            print("Paper covers Rock Computer wins!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Scissors cuts Paper Computer wins!")
        else:
            print("Paper covers Rock You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Rock breaks Scissors Computer wins!")
        else:
            print("Scissors cuts Paper You win!")

    new_game = input("Do you want to play again? (Y/N): ")
    if new_game.lower() != "y":
        break

    print("Thanks for playing Rock Paper Scissors")




