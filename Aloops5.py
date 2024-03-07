#Write a program to find the LCM of two numbers using a for loop.
n=int(input("enter the first number"))
n1=int(input("enter the 2nd number"))
product = n* n1
listn=[]
listn1=[]
list=[]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(2,n):
    if(n%i==0 and is_prime(i)):
        listn.append(i)
for k in range(2,n1):
    if(n1%k==0 and is_prime(k)):
        listn1.append(k)
for k in listn:
    for j in listn1:
        if(k==j):
            list.append(k)
produc=1
for i in range(0,len(list)):
    produc=produc+list[i]
GCD= produc
LCM = product/GCD
print(f"{GCD} is the GCD  of the {n} and {n1}")
print(f"{LCM} is the LCM  of the {n} and {n1}")

