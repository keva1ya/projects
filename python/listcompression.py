
a="hello world"
list=[x for x in a]

list2=[x for x in range(200) if x%2==0]

list3=[x**2 for x in range(100)]

list4=[x for x in range(200) if x%3==0 or x%5==0 or x%7==0]

y="one 1 two 2"
list5=[x for x in y if x.isnumeric()]
print(list5)
list6=[x for x in y if x.isalpha()]
print(list6)