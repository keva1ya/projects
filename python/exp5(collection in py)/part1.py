n = int(input("enter the number of fruits in each set: "))


s1 = set()
print(f"enter {n} fruit names for s1:")
for i in range(n):
    f = input(f"fruit {i+1}: ")
    s1.add(f.lower())
s2 = set()
print(f"enter {n} fruit names for s2:")
for i in range(n):
    f = input(f"fruit {i+1}: ")
    s2.add(f.lower())
commonf = s1.intersection(s2)
print("fruits in both sets:", commonf)
onlyf = s1.difference(s2)
print("fruits only in s1:", onlyf)
allf = s1.union(s2)
print("total number of unique fruits:", len(allf))
