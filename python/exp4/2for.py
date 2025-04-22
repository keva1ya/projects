n = 153
num = len(str(n))
sum = 0

for digit in str(n):
    sum += int(digit) ** num

if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
