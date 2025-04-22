#write a program to find largest elemnt in dict/tuple
x={2,3,4,5,6,7,8,9,10}
y=(2,3,4,5,6,7,8,9,10)
i=0
maxd=0  
for i in x:
    if i>maxd:
        maxd=i
print(maxd)
maxt=0
k=0
for k in y:
    if k>maxt:
        maxt=k
print(maxt)