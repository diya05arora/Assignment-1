# Write a python program that calculates the sum of the digits of a given number.
num = int(input("Enter a number to calculate the sum of its digits: "))
temp = num
sum = 0
while(temp>0):
    sum = sum + temp%10
    temp = temp//10
print("The sum of all the digits of", num, "=", sum) 