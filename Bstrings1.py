# reverse the string
n="umamahesh"
list=[]
list1=[]
list2=[]
for i in n:
    list.append(i)
print(list)
print(f"len(list) is {len(list)}")
for j in range(len(list)-1,-1,-1):
    list1.append(list[j])
print(list1)
k=len(list1)-1
for t in range(0,2*k):
    for m in range(0,len(list1)):

        if(t%2==0):
            list2.append(list1[m])
        elif(t%2!=0):
            list2.append(" ")
reverse_string=" ".join(list2)
print(n)
print(f"the reversed string is {reverse_string}")



    
