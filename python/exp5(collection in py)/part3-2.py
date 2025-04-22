x = int(input("Enter the number of values in the set: "))
s1 = []

print(f"Enter {x} values for s1 (allowed only 0 to 3):")
for i in range(x):
    while True:
        value = int(input(f"Value {i + 1}: "))
        if 0 <= value <= 3:
            s1.append(value)
            break
        else:
            print("invalid input, enter a value between 0 and 3")

n = int(input("Value to search for: "))
print(f"Frequency of {n} is", s1.count(n))
