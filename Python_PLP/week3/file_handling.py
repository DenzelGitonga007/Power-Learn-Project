# Opening a file:
# 1. Unrecommended way
# open('filename', 'mode')
file_path = 'D:/xampp/htdocs/Denzel_Projects/PLP/Python_PLP/week3/files.txt' # Get the file_path
file_handle = open(file_path, 'r')
# File handling in Python
# Get the properties of the file
print(file_handle)
# Read the file
print(file_handle.read())
# Close the file
# file_handle.close()
# Reading the content line by line
for content in file_handle:
    print(content)
print()
print("...Using the recommended way...")
print()
# 2. File context manager-- recommended way
# This closes the file automatically
# Syntax
with open(file_path, 'r') as file_handle_2:
    # Reading the content on a variable, content
    content = file_handle_2.read()
    print(content)
# Trying to write
print()
print("...Trying to write on a new file...")
with open('file_2.txt', 'w') as file_handle:
    # Write on the file
    file_handle.write("Added text")
# Open the new file
with open('file_2.txt', 'r') as file_handle:
    content = file_handle.read()
    print(content)
# Overwriting the file, file_2.txt
with open('file_2.txt', 'w') as file_handle:
    # Replace the text
    file_handle.write("The text has been replaced")
# Now open it
with open('file_2.txt', 'r') as file_handle:
    content = file_handle.read()
    print(content)
# Appending without overwriting
with open('file_2.txt', 'a') as file_handle:
    file_handle.write(" Another text has been appended")
# Open it
with open('file_2.txt', 'r') as file_handle:
    content = file_handle.read()
    print(content)