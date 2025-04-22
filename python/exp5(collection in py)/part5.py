#with lists
pnl = []
anl = []
for i in range(1000):
    if str(i) == str(i)[::-1]:
        pnl.append(i)
    nd = len(str(i))
    if sum(int(d) ** nd for d in str(i)) == i:
        anl.append(i)
print("palindrome Numbers(list):", pnl)
print("armstrong Numbers(list):", anl)
#with tuple
pnt = tuple(i for i in range(1000) if str(i) == str(i)[::-1])
ant = tuple(i for i in range(1000) if sum(int(di) ** len(str(i)) for di in str(i)) == i)
print("palindrome Numbers (tuple):", pnt)
print("armstrong Numbers (tuple):", ant)
#with list
pns = {i for i in range(1000) if str(i) == str(i)[::-1]}
ans = {i for i in range(1000) if sum(int(dig) ** len(str(i)) for dig in str(i)) == i}
print("palindrome Numbers (set):", pns)
print("armstrong Numbers (set):", ans)
