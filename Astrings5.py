#Write a program to find the longest palindromic substring in a given string.
n=input("enter any string")
list=[]
list3=[]
def find_all_substrings(n):
    for i in range(0,len(n)):
            for j in range(i+1,len(n)+1):
                print(n[i:j])
                list.append(n[i:j])
    print(list)
find_all_substrings(n)
n=input("enter any string")
def check_palindrome(n):
    list2=[]
    list1=[]
    for i in n:
        list2.append(i)
        print(list2)
    for j in range(len(list2)-1,-1,-1):
        list1.append(list2[j])
    print(list1)
    print(list1)
    if(list2==list1):
     list3.append(n)
     print("the given string is palindrome")

    else:
        print("the given string is not palindrome")
for i in list:
    check_palindrome(i)
print(f"{list3} is list3")
great=""
for i in list3:
     if(len(i)>=len(great)):
          great=i
print(f"{great} is the longest possible of the strings")



