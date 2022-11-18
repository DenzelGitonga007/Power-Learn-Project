# Having a list and printing out the values
print("...Priting out the values of a list...")
# Declare the list
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
# Sorting the list
num_list_sorted = sorted(num_list)
print("The sorted list is: ", num_list_sorted)
# Print out the values sequntially
print("The values are: ")
for values in num_list_sorted:
    print(values)
# Printing only values greater than 45
print("Over 45: ")
for over_45 in num_list_sorted:
    if over_45 > 45:
        print(over_45)
# Printing the under 45
print("Under 45: ")
for under_45 in num_list_sorted:
    if under_45 < 45:
        print(under_45)
# Enumerating to find the index and values
for count, value in enumerate(num_list_sorted):
    # Check for number 36, and print its index
    if value == 36:
        print("...Looking the position of number 36...")
        print(str(value) + " is at position " + str(count))
        break
