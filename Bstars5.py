#pyramid pattern  of stars
n = int(input("Enter any odd number (n should be greater than or equal to 2): "))

if n % 2 == 0 or n < 2:
    print("Please enter a valid odd number greater than or equal to 2.")
else:
    mid = n // 2
    for i in range(0, n):
        for j in range(n):
            if (mid - i <= j <= mid + i and i<=mid):
                print("*", end="")
            else:
                print(" ", end="")

        print()
# OR 
'''n=int(input("enter any even number"))
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
'''
''' after doing some problems in stars with 0 it is getting confuse'''