#  Write a python program that returns the minimum and maximum values in a list of numbers.
list =[]
n = int(input("Enter the number of elements you want to add in the list: "))
for _ in range(n):
    element = int(input("Enter a number to add in list: "))
    list.append(element)
print("The minimum value in the list", list, "is", min(list))
print("The maximum value in the list", list, "is", max(list))