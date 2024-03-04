import random
def user_choice():
    print("Enter your choice (rock, paper, scissor): ")
    user_choice = input().lower()
    while user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please enter rock, paper, or scissor.")
        user_choice = input().lower()
    return user_choice
def computer_choice():
    return random.choice(["rock", "paper", "scissor"])
def game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to the game: Rock, Paper, Scissor!")
while True:
    user_value = user_choice()
    computer_value = computer_choice()

    print(f"You chose {user_value}. Computer chose {computer_value}.")

    result = g(user_value, computer_value)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing. Goodbye!")
        break
