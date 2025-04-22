n = int(input("enter a number:"))
og = n
r = 0
nu = len(str(n))

for i in range(nu):
    d = n % 10
    r = r * 10 + d
    n //= 10

if og == r:
    print(og, "is a palindrome number")
else:
    print(og, "is not a palindrome number")
