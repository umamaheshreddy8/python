#Write a program to find the longest common prefix among a list of strings.
n=input("enter any string")
n1="123456789"
def check(n):
    for j in n:
        if(j  not in n1):
            print("no")
            return
    print("yes")
check(n)
    
