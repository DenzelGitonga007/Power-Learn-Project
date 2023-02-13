# Wishing you a happy valentines day

# Import time and sleep for slow typing
import sys, time
# from time import sleep
welcome_note = "💖💖💖...Welcome to Denzel's Valentines Heart Warmer 🤗🥰💖...\n...Get to celebrate your valentines in style 😲🎉🥳...\n"
for letter in welcome_note:
    time.sleep(.1) # to print slowly
    print(letter, end='')

# Get the user's name
username = input("\nNow you enter your name, dear 🤗: ")
# for letter in username:
#     time.sleep(.1)
#     print(letter, end='')

print("\nHeyyy there {} 🥰💖".format(username))

# Some charming line
pickupline = "Roses are red🌹 \n\tViolets are blue💙, \n\t\tSugar is sweet🍬, \n\t\t\tAnd so are you 💖!\n"
for letter in pickupline:
    time.sleep(.1)
    print(letter, end='')

time.sleep(2)

# PLP wishes for your valentines
plp_wishes = "\nNow, PLP also wishes to express their love towards you, {} 🤗🥰💖, isn't that sweet of them? 😉😚😍😀🤪\n".format(username)
for letter in plp_wishes:
    time.sleep(.1)
    print(letter, end='')

# Get the status of the user
status_question = "\nLet us know your current love status, dear {} 😍😀🤪".format(username)
status = ["single, ", "dating, ", "married, ", "complicated "]
for letter in status_question:
    time.sleep(.1)
    print(letter, end='')

print("\nSelect one amongst:")
for option in status:
    time.sleep(.1)
    print(option, end='')

status_selected = input("\nType your status 😍😀🤪: ")
