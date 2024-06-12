# Write a python program that checks if two strings are anagrams of each other.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
list1 = list(str1)
list2 = list(str2)
list1.sort()
list2.sort()
if(list1==list2):
    print("The given two strings", str1, "and", str2, "are the anagrams of each other!")
else:
    print("The given two strings", str1, "and", str2, "are not the anagrams of each other!")