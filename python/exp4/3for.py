num = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(num):
    print(a)
    t = a
    a = b
    b = t + b
