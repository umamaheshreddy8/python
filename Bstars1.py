#Write a Python program to print a triangle pattern of stars.
n=int(input("enter any even number"))
mid=n//2
if(n%2!=0):
    mid=(n+1)//2    
print(mid)
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<=mid and ((mid-(i-1)<=j<=(mid+(i-1))))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()