# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def mul(x,y):
#     return x*y

# def dev(x,y):
#     return x/y

# d = add(4,3)
# sub(8,4)
# mul(4,3)
# dev(8,2)
# print(d)

# import random

# def guess_the_number():
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
    
#     # Generate a random number between 1 and 100
#     number_to_guess = random.randint(1, 100)
    
#     # Set the initial attempt count to 0
#     attempts = 0
    
#     while True:
#         # Get the player's guess
#         try:
#             guess = int(input("Enter your guess: "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue
        
#         # Increase the number of attempts
#         attempts += 1
        
#         # Check the player's guess
#         if guess < number_to_guess:
#             print("Too low! Try again.")
#         elif guess > number_to_guess:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
#             break

# # Run the game
# guess_the_number()
# import random

# def get_computer_choice():
#     # Randomly select Rock, Paper, or Scissors
#     return random.choice(['Rock', 'Paper', 'Scissors'])

# def determine_winner(user_choice, computer_choice):
#     # Determine the winner based on the game rules
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
#          (user_choice == 'Scissors' and computer_choice == 'Paper') or \
#          (user_choice == 'Paper' and computer_choice == 'Rock'):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     print("Welcome to Rock, Paper, Scissors!")
    
#     while True:
#         # Get the user's choice
#         user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").capitalize()
        
#         if user_choice == 'Quit':
#             print("Thanks for playing!")
#             break
        
#         # Check if the user input is valid
#         if user_choice not in ['Rock', 'Paper', 'Scissors']:
#             print("Invalid input. Please choose Rock, Paper, or Scissors.")
#             continue
        
#         # Get the computer's choice
#         computer_choice = get_computer_choice()
#         print(f"Computer chose: {computer_choice}")
        
#         # Determine and print the winner
#         result = determine_winner(user_choice, computer_choice)
#         print(result)
        
#         # Ask if the user wants to play again
#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             print("Thanks for playing!")
#             break

# # Start the game
# play_game()


#wap a program to enter rupees in convert it into dollar
def reppes_converter():
    reppes = int(input("enter a Reuppes: "))
    


