def number_pattern(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return

    num = 1
    for i in range(1, n + 1, 2): 
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()

n = int(input("Enter an odd number: "))
number_pattern(n)
