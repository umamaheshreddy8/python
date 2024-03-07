# checking 2 strings are anagrams or not
n=input("enter the first string")
n1=input("enter the second string")
for i in n1:
    while(i not in n):
        if(i==" "):
            continue
        print("they are not anagrams")
        break
    print("they are anagrams")