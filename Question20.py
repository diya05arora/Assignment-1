# Write a python program that takes a list of numbers and returns their sum.
list =[]
n = int(input("Enter the number of elements you want to add in the list: "))
sum = 0
for _ in range(n):
    element = int(input("Enter a number to add in list: "))
    list.append(element)
    sum+=element
print("The sum of all elements of the list", list, "is", sum)