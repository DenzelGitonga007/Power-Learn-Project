# In this project, you are tasked to create a program that automates searching for a word definition in a dictionary. 
# Follow the instructions to implement
# Dictionary Project is provided here:
# We should have a data source (Download from the link above)
# Learn how to load json data into a python dictionary
# Create a function that returns a definition of a word
# Consider a condition that the entered word is not in a dictionary
# Consider input from user having different cases – upper/ lower case or mixed eg: RAIN/rain/RaIN
# Make your dictionary program more intelligent incase users input a word with wrong spelling 
# the program should be able to suggest the word that might be intended.
# eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here

# Import the JSON module and the file containing the json string
import json #the internal python json module
# Import the suggestion module-- difflib
import difflib
json_dictionary_source = open("Python_PLP\Tasks/dictionary-data-master/dictionary-data-master/data.json") #the directory of the python file
# Load the json file as a dictionary in python
dictionary_source = json.load(json_dictionary_source)
# Ask the user to input any word for search
print("...Denzel Dictionary🔤...")
print("...No more struggle with words,😍 Denzel gives you hugs...😍🤗🎊")
# Search word function
def search_word(word):
    """Search for the word"""
        # Change the word into one nomalised case
    filtered_word = word.lower()
    # Check if the word exist
    try:
        # Search for the word in the dictionary_source
        for meaning in dictionary_source[filtered_word]:
            print("\nThe meaning of {} is:\n{}".format(word, meaning))
    except KeyError:
        print("Oops!🫠 🫤  Word not found... Try another search perhaps?🤔")
        # Try to put the suggestion here
        # Specify the number of close matches required, n
        n = 3
        # Accuracy, cut off
        cutoff = 0.6
        # The suggestion function
        suggestion = difflib.get_close_matches(filtered_word, dictionary_source, n, cutoff)
        print("\nYou can consider the following suggestions matching '{}'\n{}".format(word, suggestion))


#end of function search_word

# Let the program run multiple times until the user exits
rerun = "y"
while (rerun.lower() == "y"):
    # Get the input from the user
    word = input("Enter the word to search: ")
    # Call the function
    search_word(word)
    # Ask if the user wishes to continue with the program
    rerun = input("\nDo you want to search for another word?😲\n[Type y to re-search, or x to exit]: ")
# If the user doesn't want to continue
print("Okay, bye...🤗🤗🤗")
# Close the file
json_dictionary_source.close()



