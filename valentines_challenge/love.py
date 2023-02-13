# Wishing you a happy valentines day

# Import time and sleep for slow typing
import sys, time
# from time import sleep
welcome_note = "\n\n\n💖💖💖...Welcome to Denzel's Valentines Heart Warmer 🤗🥰💖...\n...Get to celebrate your valentines in style 😲🎉🥳...\n"
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
pickupline = "Roses are red🌹 \n\tViolets are blue💙, \n\t\tSugar is sweet🍬, \n\t\t\tAnd so are you 💖😀🤪!\n"
for letter in pickupline:
    time.sleep(.1)
    print(letter, end='')

time.sleep(2)

# PLP wishes for your valentines
plp_wishes = "\nNow, 🤗 PLP also wishes to express their love towards you, {} 🤗🥰💖, isn't that sweet of them? 😉😚😍😀🤪\n".format(username)
for letter in plp_wishes:
    time.sleep(.1)
    print(letter, end='')



# To allow the user to select status different times
change_status = "y"
while change_status.lower() == "y":
    # Get the status of the user
    status_question = "\nLet us know your current love status, dear {} 😍😀🤪\n".format(username)
    status = ["single, ", "dating, ", "married, ", "complicated "]
    for letter in status_question:
        time.sleep(.1)
        print(letter, end='')

    print("\nSelect one amongst:")
    for option in status:
        time.sleep(.1)
        print(option, end='')

    status_selected = input("\nType your status 😍😀🤪: ")
    if status_selected.lower() == 'single':
        plp_love_message = "\nOh, 😉😚😍, not to worry {}, as long as both Jesus and PLP love you, 😀🤪, \n\tyou shouldn't even be worried one bit about being single.\n\tHaaappppyyy Vaaallleeenntttiinnneeesss!!!😚😍😚😍\n".format(username)
        for letter in plp_love_message:
            time.sleep(.1)
            print(letter, end='')

    elif status_selected.lower() == 'dating':
        plp_love_message = "\nAwww 💖💖💖😚😍, congratulations {} 😀🤪. \n\tThat's so sweet.😍😀🤪\n\t\tPLP, and (most probably your better half 😀🤪), \n\t\t\twish you a sweeeettt and haaaappppyyy valentinesss!!!😚😍\n".format(username)
        for letter in plp_love_message:
            time.sleep(.1)
            print(letter, end='')

    elif status_selected.lower() == 'complicated':
        plp_love_message = "\nWeeellll, 😀🤪😚😍, {} 😀🤪, PLP, and (most probably your better half 😀🤪), \n\twish you a sweeeettt and haaaappppyyy valentinesss!!!😚😍\n\t\tIt's gonna be okay🤗🥰💖 ".format(username)
        for letter in plp_love_message:
            time.sleep(.1)
            print(letter, end='')
    else:
        print("\nEnjoy your valentines, {} 😀🤪😚😍".format(username))
    
    # Ask if the user wishes to continue
    change_status = input("\nWould you like to change your status another one? 😀🤪\n\n[Type y to continue or x to exit] ")
exit_statement = "\nEnjoy your valentines, {} 😀🤪😚😍".format(username)
for letter in exit_statement:
    time.sleep(.1)
    print(letter, end='')
