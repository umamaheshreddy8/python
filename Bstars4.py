#4.	Write a program to print a hollow square pattern of stars.
for i in range(0,5):
    for j in range(0,5):
            if((j>=1 and j<=3)&(i>=1 and i<=3)):
                  print(" ",end=" ")
            else:
                  print("*",end=" ")

  
    print()