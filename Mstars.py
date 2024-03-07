# python pgm to print diamond pattern 
n = int(input("Enter any odd number (n should be greater than or equal to 2): "))
n1=n-1
if n % 2 == 0 or n < 2:
    print("Please enter a valid odd number greater than or equal to 2.")
else:
    mid = n // 2
    for i in range(0, n):
        for j in range(n):
            if (mid - i <= j <= mid + i and i<=mid):
                print("*", end="")
            elif(i>mid and mid - (n1-i) <= j <= mid + (n1-i)):
                print("*", end="")
            else:
                print(" ", end="")

        print()
