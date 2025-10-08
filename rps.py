import random

# Choices
choices = ["rock", "paper", "scissors"]

# Function to decide the winner
def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

# Main game
rounds = 0

print("\n--- Rock Paper Scissors ---")
print("Game continues until YOU win!\n")

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

    if user_choice == "quit":
        print("You quit the game. Goodbye! 👋")
        break
    elif user_choice not in choices:
        print("Invalid choice. Try again!")
        continue

    computer_choice = random.choice(choices)
    rounds += 1

    print(f"\nRound {rounds}")
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie! 🤝 Try again.")
    elif result == "computer":
        print("Computer wins this round! 💻")
    else:
        print(f"🎉 You won in {rounds} round(s)! 🏆")
        break