# Create a dictionary named personalDetails with the following information ( 5 marks)
# FisrtName James, LastName Ouko, Age 22, PhoneNumber 07123456789, Email student@gmail.com
print("...Personal details...")
# Initialize the dictionary
personalDetails = {"FirstName": "James", "LastName": "Ouko", "Age": 22, "PhoneNumber": "07123456789", "Email": "student@gmail.com"}
print("The original dictionary is: ", personalDetails)
# Update Age to 55
print("...Updating age to 55...")
new_age = {"Age": 50}
personalDetails.update(new_age)
print("With age updated: ", personalDetails)