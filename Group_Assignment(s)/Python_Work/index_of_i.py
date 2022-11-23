# Write a Python program that does the following:
# Prints the character at index i in the string "Live happily ".
# my_string = "Live happily ".
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"

print("...Get the postion of 'i'...")
# Get the string from the user
my_string = input("Enter your text: ")
# if len(my_string) != 0 and "i" in my_string:
#     # print("In '{}', 'i' is in postion {}".format(my_string, my_string.rfind('i')))
# elif "i" not in my_string:
#     print(-1)
# else:
#     print("Empty String")
if len(my_string) != 0:
    print(my_string.rfind('i'))
else:
    print("Empty string")
