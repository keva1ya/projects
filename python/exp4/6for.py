x = int(input("enter the number:"))
sum = 0
num = len(str(x))

for k in range(num):
    sum += x % 10
    x =x// 10

print("Sum of digits:", sum)
