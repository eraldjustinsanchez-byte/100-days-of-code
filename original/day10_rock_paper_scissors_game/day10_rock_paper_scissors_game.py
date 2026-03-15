import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
tie_score = 0

while True:

    player = input("\nEnter rock, paper, scissors (or 'quit' to exit): ").lower()

    if player == "quit":
        print("\nGame ended.")
        print(f"Final Score -> You: {player_score} | Computer: {computer_score} | Ties: {tie_score}")
        break

    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        tie_score += 1

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score} | Ties: {tie_score}")