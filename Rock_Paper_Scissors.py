import random

options = ["Rock", "Paper", "Scissors"]

# game loop
while True:
    # 1. input used capitalize to avoid error when not using a capital on the input
    user_choice = input("\nChoose Rock, Paper, or Scissors: ").capitalize()
    
    # input validation
    if user_choice not in options:
        print("Invalid choice! Please try again.")
        continue  # Skips the rest of the loop and asks again
        
    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")

    # Restart if input not equal yes break the loop
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again != 'y':
        print("Thanks for playing!")
        break  