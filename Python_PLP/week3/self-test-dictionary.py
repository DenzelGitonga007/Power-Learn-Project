# Create a dictionary named personalDetails with the following information ( 5 marks)
# FisrtName James
# LastName Ouko
# Age 22
# PhoneNumber 07123456789
# Email student@gmail.com
# Using the relevant properties and methods do the following;
# Update Age to 55                                       
# Print the LastName                                      
# Print length of the dictionary

# Start
print("...Personal Details...")
# Create the dictionary
personalDetails = {
    "FirstName" : "James",
    "LastName" : "Ouko",
    "Age" : 22,
    "PhoneNumber" : "07123456789",
    "Email" : "student@gmail.com"
}
# Show the initial dictionary
print("Your details at present are:",personalDetails)
# Update Age to 55
personalDetails.update(Age = 55)
print("With updated age:",personalDetails)
# Print the last name
print("Your last name is:", personalDetails.get("LastName"))