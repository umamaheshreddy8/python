#Write a function to find the minimum window in a string which contains all the characters of another string.
n1=input("enter the first string ")
n2=input("enter the second string")
listn1=[]
listn2=[]
n=""
def find_all_substrings(n):
    for i in range(0,len(n)):
            for j in range(i+1,len(n)+1):
                listn1.append(n[i:j])
    print(f"{listn1} is all occurunces of substrings in n1 string")
def function(n1,n2):
     list3=[]
     find_all_substrings(n1)
     for i in n2:
          listn2.append(i)
     print(listn2)
     
     for i in range(len(listn1)):
        flag = True
        for j in listn2:
            if j not in listn1[i]:
                flag = False
                break
        if flag:
            list3.append(listn1[i])
        least=5
        for i in list3:
             if(len(i)<least):
                  least=i
     print(f"{least} is the substring ")

     print(f"{list3} are the substrings of n1 that have windows containing all characters in n2")
function(n1,n2)
