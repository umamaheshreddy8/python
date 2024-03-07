#mirrored right-angled triangle pattern of numbers
n=int(input("enter any number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j<=n):
            print(" ",end=" ")
        else:
            print(i+j-n,end=" ")

 
    print()
 
    
    