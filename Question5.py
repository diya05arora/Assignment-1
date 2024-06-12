# Write a program that takes a string input from the user and writes it to a text file.
text = input("Enter the text to be written in a file: ")
fileObj = open("C:/Users/diya0/Machine Learning/Assignment-1/fileQ5.txt", "w")
print(text, file=fileObj)
print("Text written successfully in the file.")