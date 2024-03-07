#function to find all occurrences of a substring in a given string.\
list=[]
n1=input("enter any string")
def find_all_substrings(n):
    for i in range(0,len(n)):
            for j in range(i+1,len(n)+1):
                print(n[i:j])
                list.append(n[i:j])
    print(list)

find_all_substrings(n1)