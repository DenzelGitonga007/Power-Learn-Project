# Write a Python program to construct the following pattern, 
# using a nested for loop.

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * *

# * * *

# * *

# *


# To print upright right-angled triangle
up_limit = 5 #How many rows to ascend
for up_rows in range(0, up_limit): #print the outer asteriks
    # print(" * ")
    for up_columns in range(0, up_rows + 1):
        print("* ", end="")
    print("\r")
# To print the inverted right-angled triangle
down_limit = 5
for down_rows in range(down_limit, 0, -1):
    for down_columns in range(0, down_rows - 1):
        print("* ", end="")
    print("\r")

