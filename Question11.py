# Write a python program that generates the first n numbers in the Fibonacci sequence.
n = int(input("Enter the number of terms to be printed in fibonacci sequence: "))
x = 0
y = 1
z = x+y
print("The first", n, "terms of fibonacci sequence are:")
for _ in range(n):
    print(x, end=" ")
    x=y
    y=z
    z=x+y