for x in range(2, 101):
    is_prime = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(x)
