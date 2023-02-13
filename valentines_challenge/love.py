# Wishing you a happy valentines day

# Import time and sleep for slow typing
import sys, time
# from time import sleep
welcome_note = "💖💖💖...Welcome to Denzel's Valentines Heart Warmer 🤗🥰💖...\n...Get to celebrate your valentines in style 😲🎉🥳...\n"
for letter in welcome_note:
    time.sleep(.1) # to print slowly
    print(letter, end='')

# Get the user's name
username = input("Now you enter your name, dear 🤗: ")
for letter in username:
    time.sleep(.1)
    print(letter, end='')

print("\nHeyyy there {} 🥰💖".format(username))
