x = int(input("Enter a number: "))
a = x
r = 0
while a > 0:
    r = r * 10 + a % 10
    a = a//10

if r == x:
    print(x,"is a palindrome.")
else:
    print(x,"is not a palindrome.")
