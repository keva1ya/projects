def generate_star_pattern(n):
    mid = n // 2
    for i in range(n):
        if i == 0 or i == n - 1:
            print(" " * mid + "*")
        elif i == mid:
            print("*" + " " * (n - 2) + "*")
        else:
            spaces = abs(mid - i)
            print(" " * spaces + "*" + " " * (n - 2 * spaces - 2) + ("*" if spaces != mid else ""))
for num in range(1, 21, 2):
    print(f"\nPattern for n = {num}:\n")
    generate_star_pattern(num)
