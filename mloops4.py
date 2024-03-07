#Write a Python program to generate the Fibonacci sequence up to a certain number.
vowels=["a","e","i","o","u"]
string=input("enter the string")
list=[]
for k in string:
    for j in vowels:
        if(k==j):
            list.append(k)
print(len(list))