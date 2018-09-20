# Get the user's name
name = input("What is your name?")
# Greet the user
print("Hello, my name is CB, ChatBox not CollegeBoard. " + name + ", it is my pleasure to meet you.")
# Ask where the user is from
place = input(name + ", where are you from?")
# Reply the user by praising the place
print("Oh, " + place + ", it is a beautiful place. I wish I can visit there someday, but I can only stay in this computer.")
# Get the user's age
age = input("How old are you, " + name + "?")
# Write down the formula of the ChatBox's made-up age(100 years old) divided by the user's age
ageoverage = 100 / float(age)
# Reply with the relationship between the age
print("Funny, I am", ageoverage, "times older than you.")
# Find out the type of the user's dream house
house = input("What would be your dream house?")
# Reply with interest in the house
print("It is a very good choice.")
# Find out the cost of the house
cost = input("So, how much would this nice house cost?")
# Reply with surprise
print("Geeeeez, this is expensive.")
# Ask the user how many years the user would take the loan out to buy the house
loan = input("How many years do you plan to pay for the loan for this house?")
# Find out the annual interest rate the person expects to get the house
rate = input("And what would be the annual interest rate to buy this house? You don't need to write down the percent sign, I will deal with it for ya.")
# Write a formula to calculate the monthly payment of the house
mpymt = (((float(rate) / 100) / 12) * float(cost)) / (1 - (1 + (float(rate) / 100) / 12) ** (-float(loan) * 12))
# Write a formula to find out the total cost(car price + interest)
totalcost = float(mpymt) * float(loan) * 12
# Reply the user, telling the user the monthly payment of the house and the total cost of the house
print(name + ", after my precise calculation, your monthly payment would be " + str(mpymt) + ", and your total cost to buy the " + house + "would be " + str(totalcost) + ".")
# Say goodbye to the user
print("Ok. It has been my pleasure to meet you. I hope in the future I can see you again, " + name + ". Goodbye.")
