#printing the floyd triangle
n=int(input("enter any number"))
i=0
n1=0
while(i<n):
    n1=n1+i
    i=i+1
print(n1)
for i in range(n):
    for j in range(i):
        print(i,end=" ")
        i=i+1
    print()