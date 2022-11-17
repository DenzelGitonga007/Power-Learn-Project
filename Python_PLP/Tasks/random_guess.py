# Write a Python program to guess a number between 1 to 9.

# Note : User is prompted to enter a guess. If the user guesses
#  wrong then the prompt appears again until the guess is correct, 
#  on successful guess, user will get a "Well guessed!" message, and the program will exit.
import random
magic_number = random.randint(1, 9) # The number guessed randint
print("The magic number is: ", magic_number)
# Get the user input  and handle errors
while True:
    try:
        user_guess = int(input("Guess the magic number... enter it below: "))
        break
    except:
        print("Please enter a number only: ")
# Check whether the numbers match
while user_guess != magic_number:
    user_guess = int(input("Try another guess... enter it below: "))
# else:
print("Well guessed!")
