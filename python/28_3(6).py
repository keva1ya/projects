def star_pattern(n):
    if n % 2 == 0 or n < 1 or n > 20:
        print("Please enter an odd number between 1 and 20.")
        return
    
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if abs(mid - i) == abs(mid - j):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
for num in range(1, 21, 2):
    print(f"\nPattern for n = {num}:\n")
    star_pattern(num)
