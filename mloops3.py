#Write a Python program to find the largest element in a list.
list=[1,2,5,69,1.2]
greatestnum=0
for i in range(0,len(list)):
    if(greatestnum<=list[i]):
        greatestnum=list[i]
print(greatestnum)
