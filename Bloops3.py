#3.	Write a program to print the multiplication table of a given number.
n=int(input("enter the number"))
for i in range(1,11):
    k=i*n
    print(f"{n} * {i} = {k}")