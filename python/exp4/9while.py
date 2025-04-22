x = int(input("enter a number:"))
y = 2
p = True

while y <= x // 2:
    if x % y == 0:
        p = False
        break
    y += 1

if p and x > 1:
    print(x, "is a prime number")
else:
    print(x, "is not a prime number")
