#Write a program to remove all whitespace characters from a string.
n=input("enter a  string")
n1=""
list=[]
for i in n:
    list.append(i)
print(list)
for j in list:
    if(j==" "):
        list.remove(" ")
print(list)
for k in list:
    n1=n1+k
print(n1)
print(f"{n1} is n1")

