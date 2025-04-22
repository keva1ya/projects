
list=[x for x in range(1000) if x==sum(int(dig) ** len(str(x)) for dig in str(x))]
print(list)