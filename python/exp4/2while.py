num = int(input("Enter a number: "))
t = num
num1 = str(num)
power = len(num1)
sumpower = 0
while t > 0:
    digit = t% 10
    sumpower += digit ** power
    t //= 10
if sumpower == num:
    print(num, " is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")