n = int(input("enter the number:"))
m = 2
is_prime = True

while m <= (n // 2):
    if n % m == 0:
        is_prime = False
        break
    m += 1

if is_prime and n > 1:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
