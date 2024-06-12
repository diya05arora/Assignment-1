# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
string = input("Enter a string: ")
choice = int(input("Enter 1 to check if the string starts with given prefix\n]\
Enter 2 to check if the string ends with given suffix\n"))
if(choice==1):
    prefix=input("Enter a prefix to check if the string starts with it or not: ")
    if(string.find(prefix)==0):
        print("The string", string, "starts with the prefix", prefix)
    else:
        print("The string", string, "does not start with", prefix)
elif(choice==2):
    suffix=input("Enter a suffix to check if the string ends with it or not: ")
    if(string.find(suffix)==len(string)-len(suffix)):
        print("The string", string, "ends with the suffix", suffix)
    else:
        print("The string", string, "does not end with", suffix)
else:
    print("Wrong choice entered!")