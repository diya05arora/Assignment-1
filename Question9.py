# Write a python program that checks if a substring is present in a given string.
str = input("Enter a string: ")
substring = input("Enter a string to check whether it is present in the first string or not: ")
if(str.find(substring)!=-1):
    print("The given substring", substring, "is present in the string", str)
else:
    print("The given substring", substring, "is not present in the string", str)