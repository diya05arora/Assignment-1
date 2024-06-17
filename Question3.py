# Write a python program that calculates the factorial of a given number.
num = int(input("Enter a number to get its factorial: "))
fact=1
if(num<0):
    print("Cannot calculate the factorrial of negative number")
    fact="Infinity"
for i in range(num, 0, -1):
    fact *= i
print("The factorial of", num, "=", fact)