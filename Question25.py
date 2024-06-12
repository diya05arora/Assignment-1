# Write a program that copies the contents of one text file to another.
fileObj1 = open("C:/Users/diya0/Machine Learning/Assignment-1/file1Q25")
content = fileObj1.read()
fileObj2 = open("C:/Users/diya0/Machine Learning/Assignment-1/file2Q25", "w")
fileObj2.write(content)