#Write a Python program to check if a given number is a perfect number.
#A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. 
list=[]
n=int(input("enter a number to check"))
for i in range(2,n):
    if( i<n  and n%i==0):
        list.append(i)
print(list)
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
print(sum)
if(sum==n):
    print(f" the given {n} is perfect number")
else:
    print(f" the given {n} is  not a perfect number")



