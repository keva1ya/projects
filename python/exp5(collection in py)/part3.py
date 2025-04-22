x=int(input("enter the number of values in the set:"))
s1=[]
print(f"enter {x} values for s1:")
for i in range(x):
    value = int(input(f"value {i+1}:"))
    s1.append(value)
n=int(input("value to search for:"))
print(f"frequency of {n} is",s1.count(n))
