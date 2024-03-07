#Write a program to calculate the average of numbers in a list.
list=[1,2,3,4,5]
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
    average=sum/len(list)
print(average)

