x = input("enter a string:")
y = 0
uc = ""

while y < len(x):
    uc += x[y].upper()
    y =y+ 1

print(uc)
