# Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
birthYear = int(input("Enter your year of birth: "))
age = datetime.now().year - birthYear
print("Your age is:", age)