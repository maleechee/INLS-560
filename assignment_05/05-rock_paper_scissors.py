import random

# Main game loop
while True:
    # User choice
    user_choice = input("Enter R, P, or S for rock, paper, or scissors (or q to quit): ").lower()
    
    # Quit if user enters 'q'
    if user_choice == 'q':
        print("Thanks for playing!")
        break
    
    # Check for invalid input
    if user_choice not in ['r', 'p', 's']:
        print("Invalid input. Please enter 'R', 'P', or 'S'.")
        continue
    
    # Randomly generated choice for computer
    computer_choice = random.choice(['r', 'p', 's'])
    
    # Print choices
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f'You chose {choices[user_choice]}, Computer chose {choices[computer_choice]}')
    
    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("You lose!")