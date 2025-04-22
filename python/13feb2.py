#wap to check if given dict is monotonic or not
x={1,2,5,7,9,6}
a=[]
a.append(x)
y=a.sort()
z=a.sort(reverse=True)
if a==y or a==z:
    print("it is monotonic")
else:
    print("it is not monotonic")