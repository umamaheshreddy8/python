# check if a string is palindrome
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
     print("the given string is palindrome")

    else:
        print("the given string is not palindrome")
check_palindrome(n)