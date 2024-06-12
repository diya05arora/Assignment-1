# Write a python program that calculates the factorial of a given number.
num = int(input("Enter a number to get its factorial: "))
fact = 1
for i in range(num, 0, -1):
    fact *= i
print("The factorial of", num, "=", fact)