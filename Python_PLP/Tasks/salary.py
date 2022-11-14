# A company decided to give bonus of 5% to employee if his/her year of service is
# more than 5 years. Ask the user for their salary and year of service and
# print the net bonus amount. Write a python code to implement this scenario.
print("... Calculating salaries based on years of service...")
print(" ")
# Get the salary
while True: # Get only numerical values
    try:
        salary = int(input("Please enter your salary amount: "))
        break
    except:
        print("Kindly enter numerical values only, please...")
# Get the years of service
while True:
    try:
        years = int(input("Please key in how many years you have served the company, in numbers: "))
        break
    except:
        print("Kindly enter numerical values only, please...")
# Set the bonus calculation
bonus = 0.05 * salary
# Set the condition to print the salaries
if years > 5:
    net_bonus_salary = salary + (bonus)
    print("Your basic salary is " + str(salary))
    print("Since your years of service are more than 5, you accrue a bonus of: " + str(bonus))
    print("Hence your net bonus salary is " + str(net_bonus_salary))
else:
    print("Your salary is still {}, to accrue a bonus, you have to serve for more than 5 years".format(salary))
