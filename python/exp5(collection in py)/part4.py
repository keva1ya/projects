tup=()
list=[]
n=int(input("enter number of elements:"))
for i in range(n):
    item=int(input("enter the element:"))
    list.append(item)
tup=tuple(list)
sum=0
for i in range(n):
    sum=sum+tup[i]
print("the average is:",sum/n)