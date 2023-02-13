# Wishing you a happy valentines day

# Import time and sleep for slow typing
import sys, time
# from time import sleep
welcome_note = "💖💖💖...Welcome to Denzel's Valentines Heart Warmer 🤗🥰💖...\n...Get to celebrate your valentines in style..."
for letter in welcome_note:
    time.sleep(.1)
    print(letter.encode("utf-8"), end='')
