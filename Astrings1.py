#11.Write a Python function to perform string compression by replacing repeated characters with their count.
n=input("enter a string ")
list=[]
for i in n:
    list.append(i)
print(list)
for i in range( len(list)):
     count=list.count(list[i])
     print(f" the {list[i]} is repeated {count} times")
     if(count>1):
          list.remove(list[i])
          list.insert(i,count)

 
print(list)
n1=""
for i in list:
     n1=n1+str(i)
print(f"{n1} is the new  string")
          
