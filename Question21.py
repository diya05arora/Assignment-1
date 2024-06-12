# Write a python program that counts the occurrences of a specific element in a list
list =[]
n = int(input("Enter the number of elements you want to add in the list: "))
for _ in range(n):
    element = int(input("Enter a number to add in list: "))
    list.append(element)
num = int(input("Enter a number to count its occurence: "))
print("The occurence of number", num, "is", list.count(num))