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
import json
json_dictionary_source = open("Python_PLP\Tasks/dictionary-data-master/dictionary-data-master/data.json")
# Load the json file as a dictionary in python
dictionary_source = json.load(json_dictionary_source)

# Try and iterate through the data inside the file-- dictionary_source
for word in dictionary_source["abandoned industrial site"]:
    print(word)

# Get the keys
# print(dictionary_source.keys())

