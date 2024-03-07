#finding the longest common prefix among a list of strings.
list= ["python", "pyramid", "pyromaniac", "pythagorean"]
list1=[]
list2=[]
def find_prefix(n):
     for i in range(1,len(n)+1):
          print(n[0:i])
          list1.append(n[0:i])
for i in list:
     find_prefix(i)
print(list1)
for i in list1:
     count=list1.count(i)
     if(count==len(list)):
          list2.append(i)
     print(f"{count} is for {i}")
print(list2)
great=''
for i in list2:
     if(len(i)>=len(great)):
          great=i
print(f"{great} is the longest prefix of the strings")


