# Write a program that reads data from a CSV file and prints it to the console
import csv
fileObj = open("C:/Users/diya0/Machine Learning/Assignment-1/train.csv")
reader = csv.reader(fileObj)
print("Data in CSV file: ")
for data in reader:
    print(data)